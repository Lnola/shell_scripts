## Purpose

TBA

## Config

### ~/.zshrc

Open the file with the following

```sh
$ cd ~
$ vim .zshrc
```

Add this to the bottom of the file

```sh
# <<<<< CUSTOM SHELL SCRIPTS >>>>>

# To add a new subfolder access just add the name to the list
sub_folders=("/" "group1" "group2" "group3")

# Add all ~/bin/ subfolders to path
for sub_folder in "${sub_folders[@]}"; do
    export PATH="$HOME/bin/$sub_folder:$PATH"
done

# Add a prefix to all files in the subfolder
prefix="g1"
subfolder="group1"
for file in ~/bin/$subfolder/*.sh; do
    filename=$(basename "$file" .sh)
    alias "${prefix}_${filename}"="$file"
done

# <<<<< CUSTOM SHELL SCRIPTS >>>>>
```

### ~/bin

Example file structure (all `/group1` files will have the `g1_` prefix)

```sh
bin
├── group1
│   ├── script1.sh
│   └── script2.sh
├── group2
│   └── script3.sh
└── group3
    ├── script4.sh
    └── script5.sh
```

## Example usage

The commands are global, meaning you can use them from any folder on the system (based on the user since they are stored in `~/bin`)

```sh
$ cd ~
$ g1_script1
$ g1_script2
$ script3
$ script4
$ script5

$ cd Documents
$ g1_script1
$ g1_script2
$ script3
$ script4
$ script5
```

## To add a new script...

1. Create a test script and place it inside the `~/bin/*` folder
2. If it is a new folder add it to the list in the `~/.zshrc` (described in detail above)
3. Run the following command to configure permissions for the file

```sh
$ chmod +x ~/bin/${folder}/${filename}
```

4. Run the following command to apply the changes

```sh
$ source ~/.zshrc
```

5. Run the command from anywhere!
