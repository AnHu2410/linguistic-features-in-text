import importlib_resources
import sys

def func():
    sys.path.insert(0, '..')
    text = importlib_resources.files("shared_resources/resources/connectives/connectives_de.txt").read_text()
    print(text)

if __name__ == "__main__":
    func()