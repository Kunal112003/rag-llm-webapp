# prompt.py

recipe_prompt = '''
User Request: {query}

Format:
- Dish Name: 
- Ingredients: 
- Instructions (as a list of strings): 
- Preparation Time: 
- Difficulty Level:

'''

cuisine_prompt = '''
User Request: {query}

Format:
- cuisine_name:
- description:
- popular_dishes:
- cooking_techniques:

{format_instructions}
'''

tips_prompt = '''
User Request: {query}

Format:
- tips:
- common_mistakes:
- best_ingredients:

{format_instructions}
'''
