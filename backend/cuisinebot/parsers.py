# parsers.py
from pydantic import BaseModel, Field, Extra
from typing import List, Optional

class Recipe(BaseModel):
    dish_name: str = Field(..., title="Dish Name")
    ingredients: List[str] = Field(..., title="Ingredients")
    instructions: List[str] = Field(..., title="Instructions")
    preparation_time: Optional[str] = Field(None, title="Preparation Time")
    difficulty_level: Optional[str] = Field(None, title="Difficulty Level")

class CuisineInfo(BaseModel):
    cuisine_name: str = Field(..., title="Cuisine Name")
    description: str = Field(..., title="Description")
    popular_dishes: List[str] = Field(..., title="Popular Dishes")
    cooking_techniques: List[str] = Field(..., title="Cooking Techniques")

class CookingTips(BaseModel):
    tips: List[str] = Field(..., title="Tips")
    common_mistakes: List[str] = Field(..., title="Common Mistakes")
    best_ingredients: List[str] = Field(..., title="Best Ingredients")
# Compare this snippet from backend/cuisinebot/prompt.py:
# # prompt.py
#
# recipe_prompt = '''
# User Request: {query}
#
# Format:
# - Dish Name:
# - Ingredients:
# - Instructions (as a list of strings):
# - Preparation Time:
# - Difficulty Level:
#
