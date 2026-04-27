from __future__ import annotations

import ast
import operator
from typing import Any, Dict

ALLOWED_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

ALLOWED_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def safe_eval(expression: str, variables: Dict[str, Any]) -> Any:
    tree = ast.parse(expression, mode="eval")
    return _eval_node(tree.body, variables)


def _eval_node(node: ast.AST, variables: Dict[str, Any]) -> Any:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only int/float constants are allowed")
    if isinstance(node, ast.Name):
        if node.id not in variables:
            raise ValueError(f"Unknown variable: {node.id}")
        value = variables[node.id]
        if not isinstance(value, (int, float)):
            raise ValueError(f"Variable must be numeric: {node.id}")
        return value
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in ALLOWED_BIN_OPS:
            raise ValueError(f"Unsupported operator: {op_type.__name__}")
        return ALLOWED_BIN_OPS[op_type](
            _eval_node(node.left, variables),
            _eval_node(node.right, variables),
        )
    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in ALLOWED_UNARY_OPS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        return ALLOWED_UNARY_OPS[op_type](_eval_node(node.operand, variables))
    raise ValueError(f"Unsupported syntax: {type(node).__name__}")
