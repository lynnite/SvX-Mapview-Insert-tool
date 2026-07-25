import re
import os

input_filename = "inserts.yml"
output_filename = "inserts.yml"

def filename_to_pascal_case(path_str):
    """
    Extracts filename from path and converts snake_case/kebab-case 
    to PascalCase. Example: "/path/gym_alternate.yml" -> "GymAlternate"
    """
    path_str = path_str.strip('"\'')
    base_name = os.path.splitext(os.path.basename(path_str))[0]
    words = re.split(r'[-_]', base_name)
    return "".join(word.capitalize() for word in words)

def process_yml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    output_lines = []
    
    entity_blocks = re.split(r'(?=\n-\s*type:\s*entity)', content)

    for block in entity_blocks:
        if not block.strip():
            continue

        id_match = re.search(r'^\s*id:\s*([^\n]+)', block, re.MULTILINE)
        if not id_match:
            continue

        main_id = id_match.group(1).strip()

        variations = re.findall(
            r'-\s*spawn:\s*([^\n]+)[\s\S]*?probability:\s*([^\n]+)', 
            block
        )

        if not variations:
            continue

        output_lines.append(f"- id: {main_id}")

        if len(variations) == 1:
            _, prob_val = variations[0]
            output_lines.append(f"  chance: {prob_val.strip()}")
            output_lines.append("  direction: north")

        else:
            output_lines.append("  direction: north")
            output_lines.append("  variations:")
            for spawn_path, prob_val in variations:
                var_id = filename_to_pascal_case(spawn_path)
                output_lines.append(f"    - id: {var_id}")
                output_lines.append(f"      chance: {prob_val.strip()}")

        output_lines.append("")

    return "\n".join(output_lines)

cleaned_yaml = process_yml(input_filename)

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(cleaned_yaml)

print(f"Formatted data saved to '{output_filename}'.")