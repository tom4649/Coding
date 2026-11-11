from __future__ import annotations


class TrieNode:

    def __init__(self):
        self.is_file = False
        self.children: dict[str, TrieNode] = {}
        self.contents = []


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def _split_path(self, path):
        return [p for p in path.split("/") if p]

    def search(self, path):
        parts = self._split_path(path)
        node = self.root
        for part in parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node

    def ls(self, path):
        node = self.search(path)
        if node is None:
            return []

        if node.is_file:
            parts = self._split_path(path)
            return [parts[-1]]

        return sorted(node.children.keys())

    def mkdir(self, path):
        parts = self._split_path(path)
        node = self.root
        for part in parts:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]

    def addContentToFile(self, filePath, content):
        parts = self._split_path(filePath)
        node = self.root
        for part in parts[:-1]:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]

        file_name = parts[-1]
        if file_name not in node.children:
            node.children[file_name] = TrieNode()

        file_node = node.children[file_name]
        file_node.is_file = True
        file_node.contents.append(content)

    def readContentFromFile(self, filePath):
        node = self.search(filePath)
        if node and node.is_file:
            return "".join(node.contents)
        return ""


def execute(operations: list[list[str]]) -> list[str]:
    filesystem = FileSystem()
    results = []

    for operation, *args in operations:
        if operation == "FileSystem":
            continue
        elif operation == "ls":
            results.extend(filesystem.ls(*args))
        elif operation == "mkdir":
            filesystem.mkdir(*args)
        elif operation == "addContentToFile":
            filesystem.addContentToFile(args[0], " ".join(args[1:]))
        elif operation == "readContentFromFile":
            results.append(filesystem.readContentFromFile(*args))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return results

if __name__ == "__main__":
    operations = [input().split() for _ in range(int(input()))]
    res = execute(operations)
    print(" ".join(res))
