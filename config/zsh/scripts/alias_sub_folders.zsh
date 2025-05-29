# To add a new subfolder access just add the name in the list
sub_folders=()

for sub_folder in "${sub_folders[@]}"; do
    # Add all ~/bin/ subfolders to path
    export PATH="$HOME/bin/$sub_folder:$PATH"

    # Add root files in sub_folders to alias
    for file in "$HOME/bin/$sub_folder/"*.sh; do
        filename=$(basename "$file" .sh)
        alias "$filename"="$file"
    done
done

alias avstd="av start:dev"
alias avsti="av start:infra"
alias ave2e="av test:e2e"
alias avstp="av stop"
alias avrms="av migration:seed"
alias avstl="av start:learning"
alias avtd="av turbo:dev"
