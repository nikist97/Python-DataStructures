"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Implementation for many math related algorithms


def fibonacci_generator(limit=None):
    """
    this method implements a generator for the fibonacci numbers
    :param limit: a limit for the generator so that it knows when to stop generating (default None - no limit)
    :return: a generator object which yields the sequence of the fibonacci number
    """

    a, b = 0, 1
    yield a

    while True:
        if b <= limit:
            yield b
        else:
            raise StopIteration
        a, b = b, a+b
