# 深度内部计划源: v23 测试、v20、每晚构建源
#   https://proposed-packages.deepin.com/
# 深度官方 北外 镜像源
#   https://mirrors.bfsu.edu.cn/deepin
# 北外源: debain/ubuntu/ubuntu-ports
#   https://mirrors.bfsu.edu.cn/
# 麒麟源
#   https://archive.kylinos.cn/kylin
# 龙芯源
#   http://pkg.loongnix.cn

mirrors = {
    'https://pkg.hamonikr.org': {
        '/': [
            'bionic',
            'bookworm',
            'bullseye',
            'entjin',
            'entsun',
            'focal',
            'groovy',
            'hanla',
            'hirsute',
            'jin',
            'public',
        ]
    },
    'https://ci.deepin.com/repo/deepin/deepin-community/': {
        "beta3": [
            "beige"
        ],
        "stable": [
            "beige"
        ],
        "beta3-dde": [
            "beige"
        ],
        "commercial": [
            "unstable"
        ],
        "driver": [
            "driver"
        ],
        "linux-libc-dev-loong64": [
            "stable"
        ],
        'moore-driver': [
            'beige'
        ]
    },
    'https://proposed-packages.deepin.com/': {
        'beige-testing': [
            'unstable'
        ],
        'dde-apricot': [
            'apricot',
            'unstable'
        ],
        'dde-nightly': [
            'bullseye',
            'dde-bullseye',
            'deepin-bullseye',
            'deepin-wine',
        ],
    },
    'https://mirrors.bfsu.edu.cn/deepin': {
        'apricot': [
            'apricot'
        ],
        'beige': [
            'beige'
        ],
    },
    'https://mirrors.bfsu.edu.cn/': {
        'debian': [
            'Debian12.4',
            'Debian11.8',
            'Debian10.13',
            'bookworm',
            'bookworm-backports',
            'bookworm-backports-sloppy',
            'bookworm-proposed-updates',
            'bookworm-updates',
            'bullseye',
            'bullseye-backports',
            'bullseye-backports-sloppy',
            'bullseye-proposed-updates',
            'bullseye-updates',
            'buster',
            'buster-backports',
            'buster-backports-sloppy',
            'buster-proposed-updates',
            'buster-updates',
            'experimental',
            'oldoldstable',
            'oldoldstable-backports',
            'oldoldstable-backports-sloppy',
            'oldoldstable-proposed-updates',
            'oldoldstable-updates',
            'oldstable',
            'oldstable-backports',
            'oldstable-backports-sloppy',
            'oldstable-proposed-updates',
            'oldstable-updates',
            'proposed-updates',
            'rc-buggy',
            'sid',
            'stable',
            'stable-backports',
            'stable-backports-sloppy',
            'stable-proposed-updates',
            'stable-updates',
            'testing',
            'testing-backports',
            'testing-proposed-updates',
            'testing-updates',
            'trixie',
            'trixie-backports',
            'trixie-proposed-updates',
            'trixie-updates',
            'unstable',
        ],
        'ubuntu': [
            'bionic',
            'bionic-backports',
            'bionic-proposed',
            'bionic-security',
            'bionic-updates',
            'devel',
            'devel-backports',
            'devel-proposed',
            'devel-security',
            'devel-updates',
            'focal',
            'focal-backports',
            'focal-proposed',
            'focal-security',
            'focal-updates',
            'jammy',
            'jammy-backports',
            'jammy-proposed',
            'jammy-security',
            'jammy-updates',
            'lunar',
            'lunar-backports',
            'lunar-proposed',
            'lunar-security',
            'lunar-updates',
            'mantic',
            'mantic-backports',
            'mantic-proposed',
            'mantic-security',
            'mantic-updates',
            'noble',
            'noble-backports',
            'noble-proposed',
            'noble-security',
            'noble-updates',
            'trusty',
            'trusty-backports',
            'trusty-proposed',
            'trusty-security',
            'trusty-updates',
            'xenial',
            'xenial-backports',
            'xenial-proposed',
            'xenial-security',
            'xenial-updates',
        ]
        ,
        'ubuntu-ports': {
            'bionic',
            'bionic-backports',
            'bionic-proposed',
            'bionic-security',
            'bionic-updates',
            'devel',
            'devel-backports',
            'devel-proposed',
            'devel-security',
            'devel-updates',
            'focal',
            'focal-backports',
            'focal-proposed',
            'focal-security',
            'focal-updates',
            'jammy',
            'jammy-backports',
            'jammy-proposed',
            'jammy-security',
            'jammy-updates',
            'lunar',
            'lunar-backports',
            'lunar-proposed',
            'lunar-security',
            'lunar-updates',
            'mantic',
            'mantic-backports',
            'mantic-proposed',
            'mantic-security',
            'mantic-updates',
            'noble',
            'noble-backports',
            'noble-proposed',
            'noble-security',
            'noble-updates',
            'trusty',
            'trusty-backports',
            'trusty-proposed',
            'trusty-security',
            'trusty-updates',
            'xenial',
            'xenial-backports',
            'xenial-proposed',
            'xenial-security',
            'xenial-updates',
        }
    },
    'https://archive.kylinos.cn/kylin/': {
        'KYLIN-ALL': [
            '10.0',
            '10.0-2101-KCM',
            '10.0-210507-yun-SZSW',
            '10.0-fixs',
            '10.0-jxsw',
            '10.0-zyj',
            '10.1',
            '10.1-0820-2',
            '10.1-2107-990-DKY',
            '10.1-2107-DKY',
            '10.1-2107-hwe-updates',
            '10.1-2107-updates',
            '10.1-2203-990-CCB',
            '10.1-2203-990-ZYD',
            '10.1-2203-CCB',
            '10.1-2203-LT',
            '10.1-2203-general-edu-updates',
            '10.1-2203-hwe-LT',
            '10.1-2203-hwe-general-edu-updates',
            '10.1-2203-hwe-updates',
            '10.1-2203-hwe-updates-preview',
            '10.1-2203-oem-hw-9006c-activation',
            '10.1-2203-oem-hw-990-activation',
            '10.1-2203-updates',
            '10.1-2203-updates-preview',
            '10.1-2209-hwe-pp-updates',
            '10.1-2209-hwe-updates',
            '10.1-2209-updates',
            '10.1-2303-XHS',
            '10.1-2303-hwe-pp-updates',
            '10.1-2303-hwe-pp-updates-preview',
            '10.1-2303-hwe-updates',
            '10.1-2303-hwe-updates-preview',
            '10.1-2303-oem-kmre',
            '10.1-2303-updates',
            '10.1-2303-updates-pre',
            '10.1-2303-updates-preview',
            '10.1-2304-tablet-updates',
            '10.1-2306-gf',
            '10.1-W525-2303-feature-preview',
            '10.1-ekylin',
            '10.1-embedded',
            '10.1-embedded-ctyun',
            '10.1-embedded-rockchip',
            '10.1-embedded-update',
            '10.1-gb18030-2022-font',
            '10.1-hwe',
            '10.1-hwe-oem-dell',
            '10.1-kirin9006C-2303-feature',
            '10.1-kirin9006C-2303-feature-preview',
            '10.1-kirin9006C-feature',
            '10.1-kirin9006C-feature-preview',
            '10.1-kirin990-2203u2-oem-hw',
            '10.1-kirin990-2303-feature',
            '10.1-kirin990-2303-feature-preview',
            '10.1-kirin990-feature',
            '10.1-kirin990-feature-preview',
            '10.1-kirinM900-2303-feature-preview',
            '10.1-kv',
            '10.1-la64',
            '10.1-oem-hp',
            '10.1-pv',
            '10.1-pw',
            '10.1-rk3588',
            '10.1-sm',
            '10.1-sw64',
            '10.1-vkylin',
            '10.1-wayland-2203-fix-disk',
            '10.1-wayland-2203-panguw',
            '10.1-wayland-2203-updates',
            '10.1-wayland-2203-updates-preview',
            '10.1-wayland-2303-updates',
            '10.1-wayland-2303-updates-preview',
            '4.0.2',
            '4.0.2-desktop',
            '4.0.2-server',
            '4.0.2sp1',
            '4.0.2sp1-desktop',
            '4.0.2sp1-server',
            '4.0.2sp2',
            '4.0.2sp2-desktop',
            '4.0.2sp2-server',
            '4.0.2sp2-server-ft2000',
            '4.0.2sp3',
            '4.0.2sp3-desktop',
            '4.0.2sp3-server',
            '4.0.2sp4',
            '4.0.2sp4-desktop',
            '4.0.2sp4-server',
            'Intel-Edu',
            'V10-GFB-020',
            'developer-kits',
        ]
    },
    'http://pkg.loongnix.cn/': {
        'loongnix': [
            'DaoXiangHu-cartoons',
            'DaoXiangHu-embedded',
            'DaoXiangHu-stable',
            'DaoXiangHu-testing',
            'DaoXiangHu-thirdparty',
        ],
        'loongnix-server' : [
            '8.3',
            '8.4',
        ]
    },
    'https://packages.microsoft.com/repos': {
        'edge': [
            'stable'    
        ],
        "vscode": [
            'stable'
        ]
    },
    "https://archive2.kylinos.cn/deb/kylin/production/": {
        "CITRIX-V10-SP1-9006C/custom/citrix/9006C-V10-SP1":[
            "default"
        ],
        "CITRIX-V10-SP1-990/custom/citrix/990-V10-SP1":[
            "default"
        ],
        "CITRIX-V10-SP1-D2000/custom/citrix/D2000-V10-SP1":[
            "default"
        ],

        "KY-V10-amd64/custom/kylin-desktop/V10-amd64": [
            "10.0",
        ],
        "KY-990-arm64/custom/kylin-desktop/990-arm64": [
            "10.1-kv",
            "default",
        ],
        "KY-9a0-arm64/custom/kylin-desktop/9a0-arm64": [
            "10.1-pv",
            "default",
        ],
        "KY-HNXX/custom/kylin-desktop-ALT/HNXX": [
            "default"
        ],
        "KY-V10-KMRE/custom/kmre/V10-KMRE/": [
            "default",
            "stable"
        ],
        "KY-V10-SP1-Eclass-amd64/custom/kylin-desktop/V10-SP1-Eclass-amd64": [
            "10.1",
            "default"
        ],
        "KY-V10-SP1-HWE-amd64/custom/kylin-desktop/V10-SP1-HWE-amd64": [
            "10.1-hwe",
            "default"
        ],
        "KY-V10-SP1-amd64/custom/kylin-desktop/V10-SP1-amd64": [
            "10.1",
            "default"
        ],
        "KY-V10-SP1-arm64/custom/kylin-desktop/V10-SP1-arm64": [
            "10.1",
            "default"
        ],
        "KY-V10-SP1-loongarch64/custom/kylin-desktop/V10-SP1-loongarch64": [
            "10.1",
            "default"
        ],
        "KY-V10-SP1-mips64el/custom/kylin-desktop/V10-SP1-mips64el": [
            "10.1",
            "default"
        ],
        "KY-V10-SP1-sw64/custom/kylin-desktop/V10-SP1-sw64": [
            "10.1-sw64",
            "default"
        ],
        "KY-V10-amd64/custom/kylin-desktop/V10-amd64": [
            "10.0",
            "default"
        ],
        "KY-V10-arm64/custom/kylin-desktop/V10-arm64": [
            "10.0",
            "default"
        ],
        "KKY-V10-mips64el/custom/kylin-desktop/V10-mips64el": [
            "10.0",
            "default"
        ],
        "KY-V4-SP1-amd64/custom/kylin-desktop/V4-SP1-amd64": [
            "default",
            "stable"
        ],
        "KY-V4-SP1-arm64/custom/kylin-desktop/V4-SP1-arm64": [
            "default",
            "stable"
        ],
        "KY-V4-SP1-mips64el/custom/kylin-desktop/V4-SP1-mips64el": [
            "default",
            "stable"
        ],
        "KY-V4-SP2-amd64/custom/kylin-desktop/V4-SP2-amd64": [
            "default",
            "stable"
        ],
        "KY-V4-SP2-arm64/custom/kylin-desktop/V4-SP2-arm64": [
            "default",
            "stable"
        ],
        "KY-V4-SP2-mips64el/custom/kylin-desktop/V4-SP2-mips64el": [
            "default",
            "stable"
        ],
        "KY-V4-SP3-amd64/custom/kylin-desktop/V4-SP3-amd64": [
            "default",
            "stable"
        ],
        "KY-V4-SP3-arm64/custom/kylin-desktop/V4-SP3-arm64": [
            "default",
            "stable"
        ],
        "KY-V4-SP3-mips64el/custom/kylin-desktop/V4-SP3-mips64el": [
            "default",
            "stable"
        ],
        "KY-V4-SP4-amd64/custom/kylin-desktop/V4-SP4-amd64": [
            "default",
            "stable"
        ],
        "KY-V4-SP4-arm64/custom/kylin-desktop/V4-SP4-arm64": [
            "default",
            "stable"
        ],
        "KY-V4-SP4-mips64el/custom/kylin-desktop/V4-SP4-mips64el": [
            "default",
            "stable"
        ],
        "KY-V4-amd64/custom/kylin-desktop/V4-amd64": [
            "default",
            "stable"
        ],
        "KY-V4-arm64/custom/kylin-desktop/V4-arm64": [
            "default",
            "stable"
        ],
        "KY-V4-mips64el/custom/kylin-desktop/V4-mips64el": [
            "default",
            "stable"
        ],
        "PART-10_1-edu/custom/partner/edu": [
            "default",
            "stable"
        ],
        "PART-10_1-edu-wayland/custom/partner/edu-wayland": [
            "default",
            "stable"
        ],
        "PART-10_1-ilscreen/custom/partner/ilscreen": [
            "default",
            "stable"
        ],
        "PART-10_1-kirin990/custom/partner/kirin990": [
            "default",
            "stable"
        ],
        "PART-10_1-kirin9a0/custom/partner/kirin9a0": [
            "default",
            "stable"
        ],
        "PART-10_1-mavis/custom/partner/mavis": [
            "default",
            "stable"
        ],
        "PART-V10/custom/partner/V10": [
            "default"
        ],
        "PART-V10-SP1/custom/partner/V10-SP1": [
            "default"
        ],
        "PART-openKylin/custom/partner/openKylin": [
            "default"
        ],
        "TEST/": [],
    },
    "https://packages.mozilla.org/": {
        "apt": [
            "mozilla"
        ]
    }
}


# https://ci.deepin.com/repo/deepin/deepin-community/
# https://proposed-packages.deepin.com/
# https://mirrors.bfsu.edu.cn/deepin
# https://mirrors.bfsu.edu.cn/
# https://archive.kylinos.cn/kylin/
# http://pkg.loongnix.cn/
# https://packages.microsoft.com/repos
# https://archive2.kylinos.cn/deb/kylin/production/
# https://packages.mozilla.org/

mirrors_translates = {
    # '深度内部计划源: v23 计划':
        # 'https://ci.deepin.com/repo/subprojects/beige',
    '深度社区自动化: v23 beta3、驱动源 (等7个子类)':
        'https://ci.deepin.com/repo/deepin/deepin-community/',
    '深度一揽子计划源: v23 测试、v20、每晚构建源':
        'https://proposed-packages.deepin.com/',
    '北外镜像: deepin V20.9、V23 beta2':
        'https://mirrors.bfsu.edu.cn/deepin',
    '北外镜像: debain/ubuntu/ubuntu-ports':
        'https://mirrors.bfsu.edu.cn/',
    '麒麟归档镜像 - (91个子类)':
        'https://archive.kylinos.cn/kylin/',
    '麒麟归档镜像 - 生产环境软件源(42个子类)':
        'https://archive2.kylinos.cn/deb/kylin/production/',
    '龙芯 loongnix 镜像源':
        'http://pkg.loongnix.cn/',
    '微软开源镜像站 - Edge、vscode':
        'https://packages.microsoft.com/repos',
    'Mozilla 镜像站 - 火狐浏览器':
        'https://packages.mozilla.org/',
    '棒子社区软件源 - pkg.hamonikr.org':
        'https://pkg.hamonikr.org',
}

# 新增源结构例如:
# 1. 单源结构
    # https://packages.microsoft.com/repos/edge/dists/stable
    #                                     ^          ^
    # 参考多源结构
# 2. 多源合并结构
    # https://mirrors.bfsu.edu.cn/debian/dists/buster
    #                            ^            ^
    # https://mirrors.bfsu.edu.cn/ubuntu/dists/jammy
    #                            ^            ^
# https://mirrors.bfsu.edu.cn
    # debian
        # bullseye
        # buster
    # ubuntu 
        # bionic
        # jammy
        
# 一些特殊的源分析
    # deb https://packages.mozilla.org/apt mozilla/main
    # firefox 源无法直接读取 url 目录