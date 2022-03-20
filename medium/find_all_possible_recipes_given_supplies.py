# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from typing import List, Set


class Ingredient:
    def __init__(self, name: str):
        self.name = name
        self.requirements = set()
        self.can_create = None

    def __repr__(self):
        return f"{self.name} {len(self.requirements)} {self.can_create}"


class Solution:
    """
    You have information about n different recipes.
    You are given a string array recipes and a 2D string array ingredients.
    The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i].
    Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

    You are also given a string array supplies containing all the ingredients that you initially have,
    and you have an infinite supply of all of them.

    Return a list of all the recipes that you can create. You may return the answer in any order.
    """

    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        def dfs(node: Ingredient) -> Set[str]:
            def helper(node: Ingredient, current_ingredients: Set[Ingredient]):
                if node.can_create:
                    return True
                if node.can_create is False:
                    return False
                if not node.requirements:
                    can_create = node.name in supplies
                    node.can_create = can_create
                    return can_create
                if node in current_ingredients:
                    return False
                current_ingredients.add(node)
                can_create = all(
                    [
                        helper(req, current_ingredients)
                        for req in node.requirements
                        if node.can_create is None
                    ]
                )
                node.can_create = can_create
                return can_create

            return helper(node, set())

        ingredient_to_node = {}
        for i, recipe_name in enumerate(recipes):
            recipe = ingredient_to_node.setdefault(recipe_name, Ingredient(recipe_name))
            for ingredient_name in ingredients[i]:
                ingredient = ingredient_to_node.setdefault(
                    ingredient_name, Ingredient(ingredient_name)
                )
                recipe.requirements.add(ingredient)

        result = []
        for recipe_name in recipes:
            recipe = ingredient_to_node[recipe_name]
            if dfs(recipe):
                result.append(recipe_name)
        print(ingredient_to_node)
        return result


r = ["bread"]
i = [["yeast", "flour"]]
s = ["yeast", "flour", "corn"]
print(Solution().findAllRecipes(r, i, s))
