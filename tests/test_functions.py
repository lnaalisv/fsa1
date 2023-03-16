import math
from record_batcher.functions import record_batcher, RECORD_MAX_SIZE_BYTES, BATCH_MAX_LENGTH, BATCH_MAX_SIZE_BYTES

def test_record_batcher_splitting():
  result = record_batcher(["a" for x in range(5000)])
  assert len(result) == (5000 / BATCH_MAX_LENGTH)

def test_record_batcher_record_skipping():
  result = record_batcher(["a", "b" * (RECORD_MAX_SIZE_BYTES +1 ), "c"])
  assert result == [["a", "c"]]

def test_record_batcher_batch_max_size():
  result = record_batcher([("a" * RECORD_MAX_SIZE_BYTES) for x in range(math.ceil(BATCH_MAX_SIZE_BYTES / RECORD_MAX_SIZE_BYTES) + 1)])
  assert len(result) == 2
