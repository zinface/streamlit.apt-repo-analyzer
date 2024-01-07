import streamlit as st
import os
import requests
import gzip
import io

from backend.streamlitsettings  import _max_width_
_max_width_()

if '_cached_' not in st.session_state.keys():
    st.session_state['_cached_'] = {}
    
@st.cache_data
def cache_get(url, spinner = True):
    if spinner:
        with st.spinner(f'加载 {url} 数据中'):
            return requests.get(url).content
    else:
        return requests.get(url).content

class ReleaseInfo:
    
    def __init__(self, url) -> None:
        if type(url) == str:
            if url.startswith('http'):
                if not url.endswith('Release'):
                    url = os.path.join(url, 'Release')
                # self.data = requests.get(url).content.decode()
                # print('request:', url)
                self.data = cache_get(url).decode(errors='ignore')
                # print('requested:', len(self.data),'size,', '[', self.data[:20], ']')
                

    def getV(self, k):
        for line in self.data.split('\n'):
            if line.startswith(k):
                return line.split(':')[1].strip()
        return 'None'
    
    def Origin(self):
        return self.getV('Origin')
    
    def Label(self):
        return self.getV('Label')
    
    def Suite(self):
        return self.getV('Suite')
    
    def Codename(self):
        return self.getV('Codename')
    
    def Version(self):
        return self.getV('Version')
    
    def Date(self):
        return self.getV('Date')
    
    def Architectures(self):
        return self.getV('Architectures')
    
    def Components(self):
        return self.getV('Components')
    # .... 待补充
    
class SourcesGzInfo:
    
    def __init__(self, url) -> None:
        if type(url) == str:
            if url.startswith('http'):
                if not url.endswith('Sources.gz'):
                    url = os.path.join(url, 'Sources.gz')
                # self.data = requests.get(url).content.decode(errors='ignore')
                # self.data = requests.get(url).content
                self.data = cache_get(url)
                # print('requested:', len(self.data),'size,', '[', self.data[:20], ']')
    
    def GetUnGzip(self):
        # buffer = io.BytesIO(self.data)
        return gzip.decompress(self.data).decode(errors='ignore')
    
    def GetPackages(self):
        pkgs = []
        
        if len(self.GetUnGzip().strip()) == 0:
            return pkgs
        
        for PackageInfo in self.GetUnGzip().strip().split('\n\n'):
            first = PackageInfo.strip().split('\n')[0]
            
            try:
                pkgs.append(first.split(':')[1].strip())
            except:
                pass

        return pkgs
    
    def GetPackageInfos(self):
        pkgInfos = []
        
        for PackageInfo in self.GetUnGzip().strip().split('\n\n'):
            pkgInfos.append(self.convByteContentPackageInfo(PackageInfo.strip()))

        return pkgInfos

    def getByteContentShortKeyWith(self, content, key: str):
        for content_line in content.split('\n'):
            if content_line.startswith(key):
                return content_line.split(':')[1].strip()

    def convByteContentPackageInfo(self, content):
        packageinfo = {
            'Package': '',
            'Format': '',
            'Binary': '',
            'Architecture': '',
            'Version': '',
            'Maintainer': '',
            'Uploaders': '',
        }

        for pk in packageinfo.keys():
            packageinfo[pk] = self.getByteContentShortKeyWith(content, pk)
        return packageinfo
    # .... 待补充

    
class PackageInfo:
    
    def __init__(self, url) -> None:
        if type(url) == str:
            if url.startswith('http'):
                if not url.endswith('Packages.gz'):
                    url = os.path.join(url, 'Packages.gz')
                # self.data = requests.get(url).content.decode(errors='ignore')
                # self.data = requests.get(url).content
                self.data = cache_get(url)
                # print('requested:', len(self.data),'size,', '[', self.data[:20], ']')
    
    def GetUnGzip(self):
        # buffer = io.BytesIO(self.data)
        return gzip.decompress(self.data).decode(errors='ignore')
    
    def GetPackages(self):
        pkgs = []
        
        if len(self.GetUnGzip().strip()) == 0:
            return pkgs
        
        # 不得不说，kylin 的 Packages 可能不止两个 \n
        for PackageInfo in self.GetUnGzip().strip().split('\n\n'):
            first = PackageInfo.strip().split('\n')[0]

            try:
                pkgs.append(first.split(':')[1].strip())
            except:
                pass

        return pkgs
    
    def GetPackageInfos(self):
        pkgInfos = []
        
        for PackageInfo in self.GetUnGzip().strip().split('\n\n'):
            pkgInfos.append(self.convByteContentPackageInfo(PackageInfo))

        return pkgInfos

    def getByteContentShortKeyWith(self, content, key: str):
        for content_line in content.split('\n'):
            if content_line.startswith(key):
                return ':'.join(content_line.split(':')[1:]).strip()

    def convByteContentPackageInfo(self, content):
        packageinfo = {
            'Package': '',
            'Architecture': '',
            'Version': '',
            'Maintainer': '',
            'Installed-Size': '',
            'Homepage':'',
            'Filename': '',
        }

        for pk in packageinfo.keys():
            packageinfo[pk] = self.getByteContentShortKeyWith(content, pk)
        return packageinfo
    # .... 待补充


from backend.repomirrors import mirrors

def check_url(url):
    return requests.head(url).status_code == 200

# 预期优先显示的架构名称
priority_arch = st.sidebar.text_input('填写我的架构 - 优先显示', placeholder='例如: amd64、arm64、riscv64', value='amd64').strip()
priority_package = st.sidebar.text_input('填写我的包 - 优先显示', placeholder='例如: linux-images').strip()

mirror = st.sidebar.selectbox('选择镜像源', options=mirrors.keys())
prefix = mirror
dists = mirrors[mirror]

release = st.sidebar.selectbox('选择发行版', options=dists.keys())
dist = st.sidebar.selectbox('选择发行源', options=dists[release])

repo_prefix_url = os.path.join(prefix, release, 'dists', dist)
st.text(repo_prefix_url)
rinfo = ReleaseInfo(repo_prefix_url)

st.info('架构成分: ' + rinfo.Architectures() +', 组件成分: ' + rinfo.Components())

try:
    priority_arch_index = 0
    if priority_arch != '':
        priority_arch_index = rinfo.Architectures().split().index(priority_arch)
except ValueError:
    st.warning(f'没有预期的架构: {priority_arch}')

arch = st.selectbox('选择架构', options=rinfo.Architectures().split(' '), index=priority_arch_index)
comp = st.selectbox('选择组件', options=rinfo.Components().split(' '))

repo_comp_source_url = os.path.join(repo_prefix_url, comp, 'source')
repo_comp_binary_url = os.path.join(repo_prefix_url, comp, f'binary-{arch}')
st.text(repo_comp_source_url)
st.text(repo_comp_binary_url)

if check_url(repo_comp_binary_url + '/'):
    with st.spinner('加载中'):
    # sinfo = SourcesGzInfo(repo_comp_source_url)
        pinfo = PackageInfo(repo_comp_binary_url)
        packages = pinfo.GetPackages()
        packages.sort()
        priority_package_index = 0
        for i, pkg in enumerate(packages):
            if priority_package in pkg:
                priority_package_index = i
                break
        package = st.selectbox('选择包', packages, index = priority_package_index)

    with st.spinner('加载中.'):
        packageinfos = []
        for pkg in pinfo.GetPackageInfos():
            if pkg['Package'] == package and package != None:
                packageinfos.append(pkg)
    
        if st.sidebar.checkbox('软件包列表显示切换'):
            for pkg in packageinfos:
                # name = os.path.basename(pkg['Filename'])
                deb_url = os.path.join(prefix, release, pkg['Filename'])
                # pkg['Filename'] = f'<a href="{deb_url}">下载软件包: {name}</a>'
                # pkg['Download'] = deb_url
                pkg['Filename'] = deb_url

            st.dataframe(packageinfos, column_config={
                'Filename': st.column_config.LinkColumn('Download')
            }, height=500)
        else:
            for pkg in packageinfos:
                st.table(pkg)
                name = os.path.basename(pkg['Filename'])
                deb_url = os.path.join(prefix, release, pkg['Filename'])
                st.markdown(f'<a href="{deb_url}">下载软件包: {name}</a>', unsafe_allow_html=True)
else:
    st.warning('此组件架构无内容')