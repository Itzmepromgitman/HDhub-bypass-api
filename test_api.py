"""Test the API bypass functionality with HubCloud link."""
from api.index import bypasser

# Test with HubCloud link (link_2)

test_url = "https://gadgetsweb.xyz/?id=Q1dxTzFnbjhrQm5kMG5lL01tQzcvZzhmMjZOTkNrdktvSEp1VXBaU3FnZjZhRkRCdkxtZG5oY1NMak84L0xhWjNyVklCRlIwS1FQWENHbWprV1A5eGc9PQ=="

print("Testing HubCloud bypass...")
result = bypasser.bypass_gadgetsweb(test_url)

if result.get("final_url"):
    print("[OK] SUCCESS!")
    print(f"   Final: {result['final_url'][:100]}...")
else:
    print(f"[FAIL] Error: {result.get('error', 'Unknown error')}")

