

class ProductHandler:
    """
    Gets products by id or sku or by category
    """

    def __init__(self, config):
        self._config = config

    def get_product_by_id(self, product_id):
        """
        Gets the product by id if a valid id is passed, else returns None
        :param product_id: product id
        :return: product dict
        """
        return {}

    def get_products_by_category(self, category):
        """
        Gets all products in the passed in category
        :param category: product category
        :return: list of product dict
        """
        return [{"name":"my test product", "category": category}]
