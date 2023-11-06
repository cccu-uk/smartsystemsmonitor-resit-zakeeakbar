# Log Rotation Script
rotateLogs () {
    SIZE=$ (WC -1|awk '{print}')
    COUNT_LOG_FILES=$ (ls      |   grep    ".*.gz"   |   wc -1)
    echo    
    if  [[   -gt 1500 ]]; then
    mv .1.gz .2.gz || continue # if ! exist ignore logger "ace:rotateLogs" "rotating log shifting by 1"
    gzip -c  > .1.gz
    resetlog
    :fi
