import ast


def constant_folding(node):
    if isinstance(node, ast.BinOp):
        left_value = constant_folding(node.left)
        right_value = constant_folding(node.right)
        if isinstance(left_value, (int, float)) and isinstance(
            right_value, (int, float)
        ):
            try:
                return eval(f"{left_value} {node.op} {right_value}")
            except ZeroDivisionError:
                print("Warning: Division by zero detected.")
                return None
    elif isinstance(node, ast.UnaryOp):
        operand_value = constant_folding(node.operand)
        if isinstance(operand_value, (int, float)):
            return eval(f"{node.op} {operand_value}")
    elif isinstance(node, ast.Num):
        return node.n
    return node


def dead_code_elimination(node):
    if isinstance(node, ast.If):
        condition_value = constant_folding(node.test)
        if condition_value is not None:
            if condition_value:
                return dead_code_elimination(node.body[0])
            elif len(node.orelse) > 0:
                return dead_code_elimination(node.orelse[0])
    elif isinstance(node, ast.Expr):
        return dead_code_elimination(node.value)
    elif isinstance(
        node,
        (
            ast.Module,
            ast.FunctionDef,
            ast.ClassDef,
            ast.AsyncFunctionDef,
            ast.For,
            ast.While,
            ast.AsyncFor,
            ast.With,
            ast.AsyncWith,
        ),
    ):
        node.body = [dead_code_elimination(stmt) for stmt in node.body]
    return node


def optimize_code(code):
    tree = ast.parse(code)
    tree = constant_folding(tree)
    tree = dead_code_elimination(tree)
    optimized_code = compile(tree, filename="<ast>", mode="exec")
    return optimized_code


def main():
    original_code = """
x = 2 + 3
y = x * 4
if False:
    y = y + 1
print(y)
"""

    print("Original Code:")
    print(original_code)

    optimized_code = optimize_code(original_code)

    print("\nOptimized Code:")
    exec(optimized_code)


if __name__ == "__main__":
    main()
