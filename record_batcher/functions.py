RECORD_MAX_SIZE_BYTES =  1 * 1024 * 1024
BATCH_MAX_SIZE_BYTES = 5 * 1024 * 1024
BATCH_MAX_LENGTH = 500

def _record_batcher(records: list[str], copy = False) -> list[list[str]]:
    batches = []
    current_batch = []
    current_batch_length = 0

    for index in range(len(records)):
        record = records[index]
        # use naive, maybe not 100% accurate way of determining record size
        # perhaps enough for this exercise
        record_size = len(record.encode('utf-8'))
 
        # drop too big records
        if record_size > RECORD_MAX_SIZE_BYTES:
            continue
        
        # create new batch if current one is full
        if (current_batch_length + record_size) > BATCH_MAX_SIZE_BYTES or len(current_batch) == BATCH_MAX_LENGTH:
            batches.append(current_batch)
            current_batch = []
            current_batch_length = 0
        current_batch_length += record_size
        current_batch.append(record[:] if copy else record)

    batches.append(current_batch)
    return batches

# Splits the given list of records into lists of max length BATCH_MAX_LENGTH
# records bigger than RECORD_MAX_SIZE_BYTES are dropped
# batch max size in bytes is BATCH_MAX_SIZE_BYTES
def record_batcher(records: list[str]) -> list[list[str]]:
    return _record_batcher(records)

# A version of record_batcher that copies the strings instead of using the originals
def record_batcher_cpy(records: list[str]) -> list[list[str]]:
    return _record_batcher(records, True)
