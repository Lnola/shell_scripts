# ZSH

# WARNING: DO NOT CHANGE MANUALLY!
# USE THE ~/bin FOLDER INSTEAD

# To apply the changes manually run
# $ copy-file-to-destination --with-check ~/bin/config/.zsh_scripts/manage_nvmrc_with_fnm.sh ~/.zsh_scripts

autoload -U add-zsh-hook

# place default node version under $HOME/.node-version
load-nvmrc() {
  DEFAULT_NODE_VERSION=`cat $HOME/.node-version`
  if [[ -f .nvmrc && -r .nvmrc ]]; then
    fnm use
  elif [[ `node -v` != $DEFAULT_NODE_VERSION ]]; then
    echo Reverting to node from "`node -v`" to "$DEFAULT_NODE_VERSION"
    fnm use $DEFAULT_NODE_VERSION
  fi
}

add-zsh-hook chpwd load-nvmrc
load-nvmrc
