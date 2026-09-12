import sys
import xml.etree.ElementTree as ET


report = sys.argv[1] if len(sys.argv) > 1 else "reports/junit.xml"
root = ET.parse(report).getroot()

testcases = list(root.iter("testcase"))

total = len(testcases)
failed = 0
skipped = 0
failed_cases = []

for case in testcases:
    name = f"{case.attrib.get('classname', '')}::{case.attrib.get('name', '')}"

    if case.find("failure") is not None or case.find("error") is not None:
        failed += 1
        failed_cases.append(name)
    elif case.find("skipped") is not None:
        skipped += 1

passed = total - failed - skipped
pass_rate = passed / total * 100 if total else 0

print("## API 测试结果")
print()
print(f"- 总用例数: {total}")
print(f"- 通过: {passed}")
print(f"- 失败: {failed}")
print(f"- 跳过: {skipped}")
print(f"- 通过率: {pass_rate:.2f}%")

if failed_cases:
    print()
    print("### 失败用例")
    for name in failed_cases:
        print(f"- {name}")