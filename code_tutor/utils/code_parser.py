import ast

class CodeParser:
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)
        self.function_names = []
        self.class_names = []
        self.imports = []

    def parse(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                self.function_names.append(node.name)
            elif isinstance(node, ast.ClassDef):
                self.class_names.append(node.name)
            elif isinstance(node, ast.Import):
                for n in node.names:
                    self.imports.append(n.name)
            elif isinstance(node, ast.ImportFrom):
                for n in node.names:
                    self.imports.append(f"{node.module}.{n.name}")

        return self

def parse_python_code(code):
    return CodeParser(code).parse()