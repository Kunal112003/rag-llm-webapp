# agent.py
from langchain.prompts import PromptTemplate
from langchain.output_parsers import OutputFixingParser, PydanticOutputParser
from llm import LLMModels
from .parsers import Recipe, CuisineInfo, CookingTips
from .prompt import recipe_prompt, cuisine_prompt, tips_prompt
import json
import re


class CuisineAgent:
    def __init__(self, query):
        self.query = query
        self.llm = LLMModels.get_openai_model()
        self.chat_llm = LLMModels.get_openai_model()

    def get_recipe(self):
        recipe_details_prompt = '''
        User Request: {query}

        Please provide the recipe details in the following format:
        - Dish Name:
        - Ingredients: (comma-separated list) 
        - Preparation Time: 
        - Difficulty Level: 

        Please do not include any instructions here.
        '''

        instructions_prompt = '''
        User Request: {query}

        Please provide the instructions for the recipe as a list of strings:
        - Instructions: 
        '''


        # Fetching recipe details
        recipe_details_template = PromptTemplate(
            template=recipe_details_prompt,
            input_variables=["query"]
        )

        recipe_details_output = self.llm(
            recipe_details_template.format_prompt(query=self.query).to_string(),
            max_tokens=4000
        )

        # Fetching instructions
        instruction_template = PromptTemplate(
            template=instructions_prompt,
            input_variables=["query"]
        )

        instructions_output = self.llm(
            instruction_template.format_prompt(query=self.query).to_string(),
            max_tokens=4000
        )

        print("Recipe Details Output:", recipe_details_output)
        print("Instructions Output:", instructions_output)

        # Manually parse recipe details output
        recipe_details_list = recipe_details_output.splitlines()
        recipe_details_cleaned = [detail.strip() for detail in recipe_details_list if detail.strip()]

        print("Recipe Details List:", recipe_details_list)
        print("Recipe Details Cleaned:", recipe_details_cleaned)
        
        # Extracting dish name, ingredients, preparation time, and difficulty level, 
        #change 
        recipe_details = {}
        for detail in recipe_details_cleaned:
            if "Dish Name:" in detail:
                recipe_details["dish_name"] = detail.replace("Dish Name:", "").strip()
            elif "Ingredients:" in detail:
                ingredients = detail.replace("Ingredients:", "").strip()
                recipe_details["ingredients"] = [ingredient.strip() for ingredient in ingredients.split(",")]
            elif "Preparation Time:" in detail:
                recipe_details["preparation_time"] = detail.replace("Preparation Time:", "").strip()
            elif "Difficulty Level:" in detail:
                recipe_details["difficulty_level"] = detail.replace("Difficulty Level:", "").strip()

        print("Recipe Details:", recipe_details)

        # change 'dish_name': '-  Chicken Enchiladas' to 'dish_name': 'Chicken Enchiladas'
        recipe_details["dish_name"] = re.sub(r'^- ', '', recipe_details["dish_name"])
        #change 'ingredients': ['-  chicken', 'enchilada sauce'.... to 'ingredients': ['chicken', 'enchilada sauce'....
        recipe_details["ingredients"] = [re.sub(r'^- ', '', ingredient) for ingredient in recipe_details["ingredients"]]
        #change 'preparation_time': '-  30 minutes' to 'preparation_time': '30 minutes'
        recipe_details["preparation_time"] = re.sub(r'^- ', '', recipe_details["preparation_time"])
        #change 'difficulty_level': '-  Easy' to 'difficulty_level': 'Easy'
        recipe_details["difficulty_level"] = re.sub(r'^- ', '', recipe_details["difficulty_level"])



        # Manually parse instructions output
        instructions_list = instructions_output.splitlines()
        instructions_cleaned = [instruction.strip() for instruction in instructions_list if instruction.strip()]

        # Create the Recipe object
        recipe = Recipe(
            dish_name=recipe_details["dish_name"],
            ingredients=recipe_details["ingredients"],
            instructions=instructions_cleaned,
            preparation_time=recipe_details["preparation_time"],
            difficulty_level=recipe_details["difficulty_level"]
        )

        # print("Parsed Recipe:", recipe.dict())
        return recipe.dict()




    def get_cuisine_info(self):
        parser = PydanticOutputParser(pydantic_object=CuisineInfo)  
        prompt = PromptTemplate(
            template=cuisine_prompt,
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        output = self.llm(
            prompt.format_prompt(
                query=self.query,
            ).to_string()
        )

        try:
            cuisine_info = parser.parse(output)
        except Exception as e:
            print("Error during parsing:", str(e))
            fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=self.chat_llm)
            cuisine_info = fixing_parser.parse(output)

        return cuisine_info
    

        
    def get_tips(self):
        parser = PydanticOutputParser(pydantic_object=CookingTips)
        prompt = PromptTemplate(
            template=tips_prompt,
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        output = self.llm(
            prompt.format_prompt(
                query=self.query,
            ).to_string()
        )

        try:
            tips = parser.parse(output)
        except Exception as e:
            print("Error during parsing:", str(e))
            fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=self.chat_llm)
            tips = fixing_parser.parse(output)

        return tips