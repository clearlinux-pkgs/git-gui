#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : git-gui
Version  : 2.35.1
Release  : 44
URL      : https://www.kernel.org/pub/software/scm/git/git-2.35.1.tar.xz
Source0  : https://www.kernel.org/pub/software/scm/git/git-2.35.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 GPL-2.0 MIT
Requires: git-gui-bin = %{version}-%{release}
Requires: git-gui-data = %{version}-%{release}
Requires: git-gui-libexec = %{version}-%{release}
Requires: git-gui-license = %{version}-%{release}
Requires: git-gui-man = %{version}-%{release}
Requires: git = %{version}
Requires: tk
BuildRequires : asciidoc
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : expat-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : pcre2-dev
BuildRequires : perl-Error
BuildRequires : python3-dev
BuildRequires : tcl
BuildRequires : tk
BuildRequires : util-linux
BuildRequires : xmlto
BuildRequires : zlib-dev

%description
Core Git Tests
==============
This directory holds many test scripts for core Git tools.  The
first part of this short document describes how to run the tests
and read their output.

%package bin
Summary: bin components for the git-gui package.
Group: Binaries
Requires: git-gui-data = %{version}-%{release}
Requires: git-gui-libexec = %{version}-%{release}
Requires: git-gui-license = %{version}-%{release}

%description bin
bin components for the git-gui package.


%package data
Summary: data components for the git-gui package.
Group: Data

%description data
data components for the git-gui package.


%package libexec
Summary: libexec components for the git-gui package.
Group: Default
Requires: git-gui-license = %{version}-%{release}

%description libexec
libexec components for the git-gui package.


%package license
Summary: license components for the git-gui package.
Group: Default

%description license
license components for the git-gui package.


%package man
Summary: man components for the git-gui package.
Group: Default

%description man
man components for the git-gui package.


%prep
%setup -q -n git-2.35.1
cd %{_builddir}/git-2.35.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647637013
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1647637013
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/git-gui
cp %{_builddir}/git-2.35.1/COPYING %{buildroot}/usr/share/package-licenses/git-gui/3ee0019d4f4ea0a9d3f50800833f30dc14e2968e
cp %{_builddir}/git-2.35.1/compat/nedmalloc/License.txt %{buildroot}/usr/share/package-licenses/git-gui/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/git-2.35.1/contrib/persistent-https/LICENSE %{buildroot}/usr/share/package-licenses/git-gui/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/git-2.35.1/contrib/subtree/COPYING %{buildroot}/usr/share/package-licenses/git-gui/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/git-2.35.1/reftable/LICENSE %{buildroot}/usr/share/package-licenses/git-gui/29ae6b2cafd8b8dc18b829c1af20f28c24f15664
cp %{_builddir}/git-2.35.1/sha1dc/LICENSE.txt %{buildroot}/usr/share/package-licenses/git-gui/f0197ae0a546d825bcd59ba21034f36272080a4a
%make_install
## install_append content
make -C Documentation DESTDIR=%{buildroot} %{?_smp_mflags} man install
(
cd %{buildroot}
# All non-gui content is installed in the 'git' package
find ./usr -regextype egrep \! -regex '.+(gitk|git-gui).*' -delete || :
# Clean up empty dirs afterward
find ./usr -type d -empty -delete || :
)
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gitk

%files data
%defattr(-,root,root,-)
/usr/share/git-gui/lib/about.tcl
/usr/share/git-gui/lib/blame.tcl
/usr/share/git-gui/lib/branch.tcl
/usr/share/git-gui/lib/branch_checkout.tcl
/usr/share/git-gui/lib/branch_create.tcl
/usr/share/git-gui/lib/branch_delete.tcl
/usr/share/git-gui/lib/branch_rename.tcl
/usr/share/git-gui/lib/browser.tcl
/usr/share/git-gui/lib/checkout_op.tcl
/usr/share/git-gui/lib/choose_font.tcl
/usr/share/git-gui/lib/choose_repository.tcl
/usr/share/git-gui/lib/choose_rev.tcl
/usr/share/git-gui/lib/chord.tcl
/usr/share/git-gui/lib/class.tcl
/usr/share/git-gui/lib/commit.tcl
/usr/share/git-gui/lib/console.tcl
/usr/share/git-gui/lib/database.tcl
/usr/share/git-gui/lib/date.tcl
/usr/share/git-gui/lib/diff.tcl
/usr/share/git-gui/lib/encoding.tcl
/usr/share/git-gui/lib/error.tcl
/usr/share/git-gui/lib/git-gui.ico
/usr/share/git-gui/lib/index.tcl
/usr/share/git-gui/lib/line.tcl
/usr/share/git-gui/lib/logo.tcl
/usr/share/git-gui/lib/merge.tcl
/usr/share/git-gui/lib/mergetool.tcl
/usr/share/git-gui/lib/msgs/bg.msg
/usr/share/git-gui/lib/msgs/de.msg
/usr/share/git-gui/lib/msgs/el.msg
/usr/share/git-gui/lib/msgs/fr.msg
/usr/share/git-gui/lib/msgs/hu.msg
/usr/share/git-gui/lib/msgs/it.msg
/usr/share/git-gui/lib/msgs/ja.msg
/usr/share/git-gui/lib/msgs/nb.msg
/usr/share/git-gui/lib/msgs/pt_br.msg
/usr/share/git-gui/lib/msgs/pt_pt.msg
/usr/share/git-gui/lib/msgs/ru.msg
/usr/share/git-gui/lib/msgs/sv.msg
/usr/share/git-gui/lib/msgs/vi.msg
/usr/share/git-gui/lib/msgs/zh_cn.msg
/usr/share/git-gui/lib/option.tcl
/usr/share/git-gui/lib/remote.tcl
/usr/share/git-gui/lib/remote_add.tcl
/usr/share/git-gui/lib/remote_branch_delete.tcl
/usr/share/git-gui/lib/search.tcl
/usr/share/git-gui/lib/shortcut.tcl
/usr/share/git-gui/lib/spellcheck.tcl
/usr/share/git-gui/lib/sshkey.tcl
/usr/share/git-gui/lib/status_bar.tcl
/usr/share/git-gui/lib/tclIndex
/usr/share/git-gui/lib/themed.tcl
/usr/share/git-gui/lib/tools.tcl
/usr/share/git-gui/lib/tools_dlg.tcl
/usr/share/git-gui/lib/transport.tcl
/usr/share/git-gui/lib/win32.tcl
/usr/share/git-gui/lib/win32_shortcut.js
/usr/share/gitk/lib/msgs/bg.msg
/usr/share/gitk/lib/msgs/ca.msg
/usr/share/gitk/lib/msgs/de.msg
/usr/share/gitk/lib/msgs/es.msg
/usr/share/gitk/lib/msgs/fr.msg
/usr/share/gitk/lib/msgs/hu.msg
/usr/share/gitk/lib/msgs/it.msg
/usr/share/gitk/lib/msgs/ja.msg
/usr/share/gitk/lib/msgs/pt_br.msg
/usr/share/gitk/lib/msgs/pt_pt.msg
/usr/share/gitk/lib/msgs/ru.msg
/usr/share/gitk/lib/msgs/sv.msg
/usr/share/gitk/lib/msgs/vi.msg
/usr/share/gitk/lib/msgs/zh_cn.msg

%files libexec
%defattr(-,root,root,-)
/usr/libexec/git-core/git-gui
/usr/libexec/git-core/git-gui--askpass

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/git-gui/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/git-gui/29ae6b2cafd8b8dc18b829c1af20f28c24f15664
/usr/share/package-licenses/git-gui/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/git-gui/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/git-gui/3ee0019d4f4ea0a9d3f50800833f30dc14e2968e
/usr/share/package-licenses/git-gui/f0197ae0a546d825bcd59ba21034f36272080a4a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/git-gui.1
/usr/share/man/man1/gitk.1
