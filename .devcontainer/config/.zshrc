# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to oh-my-zsh installation
export ZSH="$HOME/.oh-my-zsh"

# Theme configuration
# ZSH_THEME="robbyrussell"  # Default theme
ZSH_THEME="powerlevel10k/powerlevel10k"

# Plugins
plugins=(
    git
    docker
    npm
    node
    python
    pip
    golang
    rust
    vscode
    zsh-autosuggestions
    zsh-syntax-highlighting
    zsh-completions
)

# Load Oh My Zsh
source $ZSH/oh-my-zsh.sh

# ========================================
# User Configuration
# ========================================

# Language environment
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Preferred editor
export EDITOR='vim'
export VISUAL='vim'

# ========================================
# Language-specific configurations
# ========================================

# Python
export PYTHONUNBUFFERED=1
export PIP_REQUIRE_VIRTUALENV=false

# Node.js
export NODE_ENV=development

# Go
export GOPATH=$HOME/go
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

# Rust
export PATH="$HOME/.cargo/bin:$PATH"

# ========================================
# Aliases
# ========================================

# General
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias cls='clear'
alias h='history'

# Modern CLI alternatives
alias cat='batcat'
alias find='fdfind'
alias ls='exa --icons'
alias ll='exa -l --icons'
alias la='exa -la --icons'
alias tree='exa --tree --icons'

# Git aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline --graph'
alias gd='git diff'

# Python aliases
alias py='python3'
alias pip='pip3'
alias venv='python3 -m venv'
alias activate='source venv/bin/activate'

# Node/NPM aliases
alias ni='npm install'
alias nid='npm install --save-dev'
alias nr='npm run'
alias ns='npm start'
alias nt='npm test'

# Docker aliases
alias d='docker'
alias dc='docker-compose'
alias dps='docker ps'
alias dimg='docker images'
alias dexec='docker exec -it'

# Directory navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

# ========================================
# Functions
# ========================================

# Create directory and cd into it
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Quick git commit
qcommit() {
    git add .
    git commit -m "$1"
}

# Quick git push
qpush() {
    git add .
    git commit -m "$1"
    git push
}

# Extract any archive
extract() {
    if [ -f $1 ]; then
        case $1 in
            *.tar.bz2)   tar xjf $1     ;;
            *.tar.gz)    tar xzf $1     ;;
            *.bz2)       bunzip2 $1     ;;
            *.rar)       unrar e $1     ;;
            *.gz)        gunzip $1      ;;
            *.tar)       tar xf $1      ;;
            *.tbz2)      tar xjf $1     ;;
            *.tgz)       tar xzf $1     ;;
            *.zip)       unzip $1       ;;
            *.Z)         uncompress $1  ;;
            *.7z)        7z x $1        ;;
            *)          echo "'$1' cannot be extracted" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

# FZF configuration
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# Load custom configurations if they exist
[ -f ~/.zshrc.local ] && source ~/.zshrc.local

[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh