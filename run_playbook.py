import ansible_runner

# Define the path to your playbook
playbook_path = './hello.yml'

# Create a Runner object
r = ansible_runner.RunnerConfig(private_data_dir='.', playbook=playbook_path)

# Prepare the RunnerConfig
r.prepare()

# Run the playbook
runner = ansible_runner.Runner(config=r)
result = runner.run()

