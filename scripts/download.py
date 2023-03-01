# 该脚本将 afdb 下载到本地

import wfdb

if __name__ == '__main__':
    wfdb.dl_database('afdb', './data/afdb/')
