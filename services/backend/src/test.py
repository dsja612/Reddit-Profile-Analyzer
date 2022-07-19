"""
This script conducts simple tests on the backend.
"""

import requests
import json

print('Starting test...')

print('Test 1: Suspended user u/pao')
test1 = json.loads(requests.get('http://127.0.0.1:5000/users/pao').content)
print('Test 1 passed!') if ('detail' in test1) and test1["detail"] == "User is suspended!" else print('Test 1 failed!')

print('Test 2a: Invalid username u/p')
test2a = json.loads(requests.get('http://127.0.0.1:5000/users/p').content)
print('Test 2a passed!') if ('detail' in test2a) and test2a["detail"] == "User not found!" else print('Test 2a failed!')

print('Test 2b: Invalid username (empty)')
test2b = json.loads(requests.get('http://127.0.0.1:5000/users/').content)
print('Test 2b passed!') if ('detail' in test2b) and test2b["detail"] == "Not Found" else print('Test 2b failed!')

print('Test 3a: Valid username u/Sweet_guy9')
test3a = json.loads(requests.get('http://127.0.0.1:5000/users/Sweet_guy9').content)
print('Test 3 passed!') if ('basic_data' in test3a) and ('num_comments' in test3a) else print('Test 3a failed!')

print('Test 3b: Valid username (case sensitivity) u/swEEt_gUy9')
test3b = json.loads(requests.get('http://127.0.0.1:5000/users/swEEt_gUy9').content)
print('Test 3b passed!') if ('basic_data' in test3b) and ('num_comments' in test3b) else print('Test 3b failed!')