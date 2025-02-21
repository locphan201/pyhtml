from typing import List, Literal

class Document:
    def __init__(self, content: str = 'document') -> None:
        self._content = content

    def addEventListener(self, event, callback) -> 'Document':
        self._content += f'.addEventListener("{event}", (e) => {{}})'
        return Document(self._content)

    def getElementById(self, id: str) -> 'Document':
        self._content += f'.getElementById("{id}")'
        return Document(self._content)

    def __str__(self) -> str:
        return self._content
    
    def __repr__(self) -> str:
        return self._content

class Script:
    def __init__(self):
        pass

if __name__ == '__main__':
    document = Document().getElementById('id1').getElementById('id2').addEventListener('change', [])
    print(document)