import re
from contextlib import closing

__all__ = ['validate_expression', 'gen_source']


def validate_expression(wildcard_expression):
    """
    Description:
        Validates and shortens the wild card expression(if needed) without changing the intended meaning .

    Args:
        :arg (str) wild card expression

    Returns:
        :return (str) A shortened copy of the wild card expression.

    Raises:
        :raises (``InvalidWildCardExpressionError``) Any error while validating the expression.

    Example:
        >>> from lexpy._utils import validate_expression
        >>> sample_expr = 'a*?' # Match literal `a` followed by any character Zero or unlimited times.
        >>> print(validate_expression(sample_expr)) # Outputs 'a*'

    """
    result = re.sub(r'\*+', '*', wildcard_expression)  # Replace consecutive * with single *
    result = re.sub(r'\?+', '?', result)  # Replace consecutive ? with a single ?
    result = re.sub(r'(\*\?)+', '*', result)  # Replace consecutive '*?' with a single group '*'
    return result


def gen_source(source):
    """

    """
    if hasattr(source, 'read'):
        input_file = source
    else:
        input_file = open(source, 'r')

    with closing(input_file):
        for line in input_file:
            yield line.strip()



