import os
import glob
import json
import subprocess

def execute_command(token=None):
    command = 'az devops security group list --org https://dev.azure.com/nuuvers --scope organization --subject-types aadgp'
    if token:
        command += ' --continuation-token ' + token
    return subprocess.check_output(command, shell=True).decode('utf-8')

def process_remove_line(output, deleteWord):
    lines = output.split('\n')
    lines = [line for line in lines if deleteWord not in line]
    return '\n'.join(lines)

def append_to_file(filename, data):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(data)

def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"O arquivo {file_path} foi excluído.")
    else:
        print(f"O arquivo {file_path} não existe.")



def delete_files(pattern):
    files = glob.glob(pattern)
    
    for file in files:
        try:
            os.remove(file)
            print(f"File {file} has been deleted successfully")
        except OSError as e:
            print(f"Error: {file} : {e.strerror}")



def merge_json_files(pattern, output_file):
    data = []

    files = glob.glob(pattern)

    for file in files:
        with open(file, 'r') as f:
            file_data = json.load(f)

            if "graphGroups" in file_data:
                data.extend(file_data["graphGroups"])

    with open(output_file, 'w') as f:
        json.dump(data, f)

    print(f"All JSON files matching {pattern} have been merged into {output_file}.")



def main():
    token = None
    nfile = 0
    delete_files("az-grouplist-*.json")
    while True:
        nfile = nfile + 1
        output = execute_command(token)
        output = process_remove_line(output, 'failed to get console mode for stdout: The handle is invalid.')
        data = json.loads(output)
        fileNameJson = "az-grouplist-" + str(nfile) + ".json"
        token = data['continuationToken']
        if 'continuationToken' in data and token:
            output = process_remove_line(output, 'continuationToken')
            append_to_file(fileNameJson, output)
        else:
            break

    output = process_remove_line(output, 'continuationToken')
    append_to_file(fileNameJson, output)
    merge_json_files("az-grouplist-*.json", "merged-az-grouplist.json")
    delete_files("az-grouplist-*.json")



if __name__ == '__main__':
    main()
