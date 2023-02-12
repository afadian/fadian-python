from argparse import ArgumentParser
from dataclasses import dataclass

from fadian import producer
from fadian.producers import fabing, fadian  # type: ignore

producers = producer.get_producers()


@dataclass(frozen=True)
class Arguments:
    producer: producer.Producer
    name: str
    count: int


def parse_arguments() -> Arguments:
    parser = ArgumentParser()
    parser.add_argument("--type", "-t", choices=producers.keys(), required=True)
    parser.add_argument("--name", "-n", required=True)
    parser.add_argument("--count", "-c", type=int, default=1, required=False)

    args = parser.parse_args()
    producer = producers[args.type]

    return Arguments(producer, args.name, args.count)


if __name__ == "__main__":
    args = parse_arguments()

    for _ in range(args.count):
        print(args.producer(args.name))
