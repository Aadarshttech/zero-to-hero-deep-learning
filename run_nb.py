import json
import sys
import io
import os

def run_notebook(nb_path):
    print(f"=== Testing & Executing Notebook: {nb_path} ===")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    cell_num = 0
    # Shared global namespace so cells can also build on previous state if desired,
    # but each cell has self-contained imports.
    global_ns = {}

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            cell_num += 1
            src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            print(f"Executing Code Cell {cell_num}...")
            old_stdout = sys.stdout
            redirected_output = io.StringIO()
            sys.stdout = redirected_output
            try:
                exec(src, global_ns)
                out_str = redirected_output.getvalue()
                sys.stdout = old_stdout
                cell['execution_count'] = cell_num
                cell['outputs'] = []
                if out_str:
                    cell['outputs'].append({
                        'output_type': 'stream',
                        'name': 'stdout',
                        'text': out_str.splitlines(True)
                    })
                print(f"  -> Cell {cell_num} Success! Output length: {len(out_str)} chars")
            except Exception as e:
                sys.stdout = old_stdout
                print(f"  -> ERROR in Cell {cell_num}: {e}")
                raise

    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

    print(f"SUCCESS: All {cell_num} code cells executed cleanly and outputs populated in {nb_path}!\n")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_notebook(sys.argv[1])
    else:
        print("Usage: python run_nb.py <notebook_path>")
