from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_category_iteration(self):
        # Test the __iter__ method
        recipe1 = Recipe.objects.create(
            title="Cake",
            description="A delicious chocolate cake",
            instructions="Mix and bake",
            ingredients="Flour, sugar, cocoa",
            category=self.category
        )
        recipe2 = Recipe.objects.create(
            title="Ice Cream",
            description="Homemade vanilla ice cream",
            instructions="Mix and freeze",
            ingredients="Milk, sugar, vanilla",
            category=self.category
        )
        self.assertEqual(list(iter(self.category)), [recipe1, recipe2])


class RecipeModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Cake",
            description="A delicious chocolate cake",
            instructions="Mix and bake",
            ingredients="Flour, sugar, cocoa",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(self.recipe.__str__(), self.recipe.title)

    def test_recipe_category_relationship(self):
        self.assertEqual(self.recipe.category.name, "Desserts")
        self.assertEqual(self.recipe.category, self.category)
