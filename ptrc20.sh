#!/bin/bash

if ! python3 --version; then
    echo -e "\033[31m! App requires Python3 to be installed in your system first\033[0m"
    exit 1
else
    if ! python3 scripts/check_internet.py; then
        echo -e "\033[31m! Check your internet connection and try again\033[0m"
        exit 1
    else
        pip3 install requests colorama termcolor progress
        clear
    fi
fi


printf " _____   _____   ____   _       _____  _______\n"
printf "(     | (     ) |    \ | \  /\ ( .   \ \_   _/\n"
printf "|  -  | |  |  | | /\_/ | |_/ | |  ___/   | |\n"
printf "| ----  |  |  | | \/\  |    (  | |       | |\n"
printf "| |     |     | |    \ | |-\ \ | |___    | |\n"
printf "|/      (_____) |____/ |_/  \/ (____/    (_)\n"
printf "\033[31m_______  ______  ____   _____   _____\033[0m\n"  
printf "\033[31m\_   _/ |   __/ |    \ /     \ (     )\033[0m\n"
printf "\033[31m  | |   |  |    | /\_/ \_)   / |  |  |\033[0m\n"
printf "\033[31m  | |   |  |    | \/\    /  /  |  |  |\033[0m\n"
printf "\033[31m  | |   |  |    |    \  /  (_  |     |\033[0m\n"
printf "\033[31m  (_)   |__/    |____/ (_____) (_____)\033[0m\n"
printf "\n"


info_arg=false
hash_arg=false
key=$1
case $key in
    --info)
        info_arg=true
    ;;
    -H|--hash)
        hash_arg=true
    ;;
esac

if $info_arg; then
    echo -e "\033[1;91mPocket TRC20\033[0m"
    echo -e "\033[1;90mv2.0.0\033[0m\n"
    echo -e "--info          Information menu \033[90m(current)\033[0m"
    echo -e "-H, --hash      Hash of the TRC20 transaction you want to scan\n"
    echo -e "\033[1;93mFor example:\033[0m"
    echo -e "\033[90mbash ptrc20.sh --hash 0b9cd40b4a9a36f99ba5c73527633cac6fc83a90563a3c5cf5d079dd2735f8ea\033[0m\n"
elif $hash_arg; then
    python3 scripts/scanner.py $@
else
    echo -e "\033[31m! Wrong argument or none of them were entered\033[0m"
    echo -e "Type \033[90mbash ptrc20.sh --info\033[0m for more information"
fi
