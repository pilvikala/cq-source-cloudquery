import sys
from cloudquery.sdk import serve

from plugin import CloudQueryPlugin


def main():
    p = CloudQueryPlugin()
    serve.PluginCommand(p).run(sys.argv[1:])


if __name__ == "__main__":
    main()
