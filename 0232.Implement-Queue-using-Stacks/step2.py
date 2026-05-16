class MyQueue:
    def __init__(self) -> None:
        self._enqueue_stack = []
        self._dequeue_stack = []

    def push(self, x: int) -> None:
        self._enqueue_stack.append(x)

    def pop(self) -> int:
        self._ensure_dequeue_ready()
        return self._dequeue_stack.pop()

    def peek(self) -> int:
        self._ensure_dequeue_ready()
        return self._dequeue_stack[-1]

    def empty(self) -> bool:
        return not self._enqueue_stack and not self._dequeue_stack

    def _ensure_dequeue_ready(self) -> None:
        if self._dequeue_stack:
            return
        while self._enqueue_stack:
            self._dequeue_stack.append(self._enqueue_stack.pop())
