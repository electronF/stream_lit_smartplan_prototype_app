from collections import defaultdict, deque


def merge_responses(gemini_list:list, gpt_list:list, claude_list:list):
    is_taken = defaultdict(lambda : False)
    merged_list = []
    new_gemini_list = deque(gemini_list)
    new_gpt_list = deque(gpt_list)
    new_claude_list = deque(claude_list)

    while len(new_gemini_list)>0 or len(new_gpt_list)>0 or len(new_claude_list)>0:
        if len(new_gemini_list) > 0:
            item = new_gemini_list.popleft()
            if is_taken[item['index']] == False:
                merged_list.append(item)
                is_taken[item['index']] = True
        if len(new_gpt_list) > 0:
            item = new_gpt_list.popleft()
            if is_taken[item['index']] == False:
                merged_list.append(item)
                is_taken[item['index']] = True
        if len(new_claude_list) >0:
            item = new_claude_list.popleft()
            if is_taken[item['index']] == False:
                merged_list.append(item)
                is_taken[item['index']] = True
    return merged_list


def merge_responses_1(*args):
    is_taken = defaultdict(lambda : False)
    merged_list = []
    new_lists = [deque(list_item) for list_item in args]

    while any([len(new_list)>0 for new_list in new_lists]):
        for new_list in new_lists:
            if len(new_list) > 0:
                item = new_list.popleft()
                if is_taken[item['index']] == False:
                    merged_list.append(item)
                    is_taken[item['index']] = True
    return merged_list