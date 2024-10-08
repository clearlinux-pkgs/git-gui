#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v20
# autospec commit: f35655a
#
Name     : git-gui
Version  : 2.47.0
Release  : 80
URL      : https://www.kernel.org/pub/software/scm/git/git-2.47.0.tar.gz
Source0  : https://www.kernel.org/pub/software/scm/git/git-2.47.0.tar.gz
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
BuildRequires : buildreq-configure
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
You can configure some aspects of the GitHub Actions-based CI on a
per-repository basis by setting "variables" and "secrets" from with the
GitHub web interface. These can be found at:

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
%setup -q -n git-2.47.0
cd %{_builddir}/git-2.47.0
pushd ..
cp -a git-2.47.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728407608
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728407608
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/git-gui
cp %{_builddir}/git-%{version}/COPYING %{buildroot}/usr/share/package-licenses/git-gui/3ee0019d4f4ea0a9d3f50800833f30dc14e2968e || :
cp %{_builddir}/git-%{version}/compat/nedmalloc/License.txt %{buildroot}/usr/share/package-licenses/git-gui/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/git-%{version}/contrib/persistent-https/LICENSE %{buildroot}/usr/share/package-licenses/git-gui/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/git-%{version}/contrib/subtree/COPYING %{buildroot}/usr/share/package-licenses/git-gui/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/git-%{version}/reftable/LICENSE %{buildroot}/usr/share/package-licenses/git-gui/29ae6b2cafd8b8dc18b829c1af20f28c24f15664 || :
cp %{_builddir}/git-%{version}/sha1dc/LICENSE.txt %{buildroot}/usr/share/package-licenses/git-gui/f0197ae0a546d825bcd59ba21034f36272080a4a || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/git
rm -f %{buildroot}*/usr/bin/git-receive-pack
rm -f %{buildroot}*/usr/bin/git-shell
rm -f %{buildroot}*/usr/bin/git-upload-archive
rm -f %{buildroot}*/usr/bin/git-upload-pack
rm -f %{buildroot}*/usr/bin/scalar
rm -f %{buildroot}*/usr/libexec/git-core/git
rm -f %{buildroot}*/usr/libexec/git-core/git-add
rm -f %{buildroot}*/usr/libexec/git-core/git-am
rm -f %{buildroot}*/usr/libexec/git-core/git-annotate
rm -f %{buildroot}*/usr/libexec/git-core/git-apply
rm -f %{buildroot}*/usr/libexec/git-core/git-archive
rm -f %{buildroot}*/usr/libexec/git-core/git-bisect
rm -f %{buildroot}*/usr/libexec/git-core/git-blame
rm -f %{buildroot}*/usr/libexec/git-core/git-branch
rm -f %{buildroot}*/usr/libexec/git-core/git-bugreport
rm -f %{buildroot}*/usr/libexec/git-core/git-bundle
rm -f %{buildroot}*/usr/libexec/git-core/git-cat-file
rm -f %{buildroot}*/usr/libexec/git-core/git-check-attr
rm -f %{buildroot}*/usr/libexec/git-core/git-check-ignore
rm -f %{buildroot}*/usr/libexec/git-core/git-check-mailmap
rm -f %{buildroot}*/usr/libexec/git-core/git-check-ref-format
rm -f %{buildroot}*/usr/libexec/git-core/git-checkout
rm -f %{buildroot}*/usr/libexec/git-core/git-checkout--worker
rm -f %{buildroot}*/usr/libexec/git-core/git-checkout-index
rm -f %{buildroot}*/usr/libexec/git-core/git-cherry
rm -f %{buildroot}*/usr/libexec/git-core/git-cherry-pick
rm -f %{buildroot}*/usr/libexec/git-core/git-clean
rm -f %{buildroot}*/usr/libexec/git-core/git-clone
rm -f %{buildroot}*/usr/libexec/git-core/git-column
rm -f %{buildroot}*/usr/libexec/git-core/git-commit
rm -f %{buildroot}*/usr/libexec/git-core/git-commit-graph
rm -f %{buildroot}*/usr/libexec/git-core/git-commit-tree
rm -f %{buildroot}*/usr/libexec/git-core/git-config
rm -f %{buildroot}*/usr/libexec/git-core/git-count-objects
rm -f %{buildroot}*/usr/libexec/git-core/git-credential
rm -f %{buildroot}*/usr/libexec/git-core/git-credential-cache
rm -f %{buildroot}*/usr/libexec/git-core/git-credential-cache--daemon
rm -f %{buildroot}*/usr/libexec/git-core/git-credential-store
rm -f %{buildroot}*/usr/libexec/git-core/git-daemon
rm -f %{buildroot}*/usr/libexec/git-core/git-describe
rm -f %{buildroot}*/usr/libexec/git-core/git-diagnose
rm -f %{buildroot}*/usr/libexec/git-core/git-diff
rm -f %{buildroot}*/usr/libexec/git-core/git-diff-files
rm -f %{buildroot}*/usr/libexec/git-core/git-diff-index
rm -f %{buildroot}*/usr/libexec/git-core/git-diff-tree
rm -f %{buildroot}*/usr/libexec/git-core/git-difftool
rm -f %{buildroot}*/usr/libexec/git-core/git-fast-export
rm -f %{buildroot}*/usr/libexec/git-core/git-fast-import
rm -f %{buildroot}*/usr/libexec/git-core/git-fetch
rm -f %{buildroot}*/usr/libexec/git-core/git-fetch-pack
rm -f %{buildroot}*/usr/libexec/git-core/git-fmt-merge-msg
rm -f %{buildroot}*/usr/libexec/git-core/git-for-each-ref
rm -f %{buildroot}*/usr/libexec/git-core/git-for-each-repo
rm -f %{buildroot}*/usr/libexec/git-core/git-format-patch
rm -f %{buildroot}*/usr/libexec/git-core/git-fsck
rm -f %{buildroot}*/usr/libexec/git-core/git-fsck-objects
rm -f %{buildroot}*/usr/libexec/git-core/git-fsmonitor--daemon
rm -f %{buildroot}*/usr/libexec/git-core/git-gc
rm -f %{buildroot}*/usr/libexec/git-core/git-get-tar-commit-id
rm -f %{buildroot}*/usr/libexec/git-core/git-grep
rm -f %{buildroot}*/usr/libexec/git-core/git-hash-object
rm -f %{buildroot}*/usr/libexec/git-core/git-help
rm -f %{buildroot}*/usr/libexec/git-core/git-hook
rm -f %{buildroot}*/usr/libexec/git-core/git-http-backend
rm -f %{buildroot}*/usr/libexec/git-core/git-http-fetch
rm -f %{buildroot}*/usr/libexec/git-core/git-http-push
rm -f %{buildroot}*/usr/libexec/git-core/git-imap-send
rm -f %{buildroot}*/usr/libexec/git-core/git-index-pack
rm -f %{buildroot}*/usr/libexec/git-core/git-init
rm -f %{buildroot}*/usr/libexec/git-core/git-init-db
rm -f %{buildroot}*/usr/libexec/git-core/git-interpret-trailers
rm -f %{buildroot}*/usr/libexec/git-core/git-log
rm -f %{buildroot}*/usr/libexec/git-core/git-ls-files
rm -f %{buildroot}*/usr/libexec/git-core/git-ls-remote
rm -f %{buildroot}*/usr/libexec/git-core/git-ls-tree
rm -f %{buildroot}*/usr/libexec/git-core/git-mailinfo
rm -f %{buildroot}*/usr/libexec/git-core/git-mailsplit
rm -f %{buildroot}*/usr/libexec/git-core/git-maintenance
rm -f %{buildroot}*/usr/libexec/git-core/git-merge
rm -f %{buildroot}*/usr/libexec/git-core/git-merge-base
rm -f %{buildroot}*/usr/libexec/git-core/git-merge-file
rm -f %{buildroot}*/usr/libexec/git-core/git-merge-index
rm -f %{buildroot}*/usr/libexec/git-core/git-merge-ours
rm -f %{buildroot}*/usr/libexec/git-core/git-merge-recursive
rm -f %{buildroot}*/usr/libexec/git-core/git-merge-subtree
rm -f %{buildroot}*/usr/libexec/git-core/git-merge-tree
rm -f %{buildroot}*/usr/libexec/git-core/git-mktag
rm -f %{buildroot}*/usr/libexec/git-core/git-mktree
rm -f %{buildroot}*/usr/libexec/git-core/git-multi-pack-index
rm -f %{buildroot}*/usr/libexec/git-core/git-mv
rm -f %{buildroot}*/usr/libexec/git-core/git-name-rev
rm -f %{buildroot}*/usr/libexec/git-core/git-notes
rm -f %{buildroot}*/usr/libexec/git-core/git-pack-objects
rm -f %{buildroot}*/usr/libexec/git-core/git-pack-redundant
rm -f %{buildroot}*/usr/libexec/git-core/git-pack-refs
rm -f %{buildroot}*/usr/libexec/git-core/git-patch-id
rm -f %{buildroot}*/usr/libexec/git-core/git-prune
rm -f %{buildroot}*/usr/libexec/git-core/git-prune-packed
rm -f %{buildroot}*/usr/libexec/git-core/git-pull
rm -f %{buildroot}*/usr/libexec/git-core/git-push
rm -f %{buildroot}*/usr/libexec/git-core/git-range-diff
rm -f %{buildroot}*/usr/libexec/git-core/git-read-tree
rm -f %{buildroot}*/usr/libexec/git-core/git-rebase
rm -f %{buildroot}*/usr/libexec/git-core/git-receive-pack
rm -f %{buildroot}*/usr/libexec/git-core/git-reflog
rm -f %{buildroot}*/usr/libexec/git-core/git-remote
rm -f %{buildroot}*/usr/libexec/git-core/git-remote-ext
rm -f %{buildroot}*/usr/libexec/git-core/git-remote-fd
rm -f %{buildroot}*/usr/libexec/git-core/git-remote-ftp
rm -f %{buildroot}*/usr/libexec/git-core/git-remote-ftps
rm -f %{buildroot}*/usr/libexec/git-core/git-remote-http
rm -f %{buildroot}*/usr/libexec/git-core/git-remote-https
rm -f %{buildroot}*/usr/libexec/git-core/git-repack
rm -f %{buildroot}*/usr/libexec/git-core/git-replace
rm -f %{buildroot}*/usr/libexec/git-core/git-rerere
rm -f %{buildroot}*/usr/libexec/git-core/git-reset
rm -f %{buildroot}*/usr/libexec/git-core/git-restore
rm -f %{buildroot}*/usr/libexec/git-core/git-rev-list
rm -f %{buildroot}*/usr/libexec/git-core/git-rev-parse
rm -f %{buildroot}*/usr/libexec/git-core/git-revert
rm -f %{buildroot}*/usr/libexec/git-core/git-rm
rm -f %{buildroot}*/usr/libexec/git-core/git-send-pack
rm -f %{buildroot}*/usr/libexec/git-core/git-sh-i18n--envsubst
rm -f %{buildroot}*/usr/libexec/git-core/git-shell
rm -f %{buildroot}*/usr/libexec/git-core/git-shortlog
rm -f %{buildroot}*/usr/libexec/git-core/git-show
rm -f %{buildroot}*/usr/libexec/git-core/git-show-branch
rm -f %{buildroot}*/usr/libexec/git-core/git-show-index
rm -f %{buildroot}*/usr/libexec/git-core/git-show-ref
rm -f %{buildroot}*/usr/libexec/git-core/git-sparse-checkout
rm -f %{buildroot}*/usr/libexec/git-core/git-stage
rm -f %{buildroot}*/usr/libexec/git-core/git-stash
rm -f %{buildroot}*/usr/libexec/git-core/git-status
rm -f %{buildroot}*/usr/libexec/git-core/git-stripspace
rm -f %{buildroot}*/usr/libexec/git-core/git-submodule--helper
rm -f %{buildroot}*/usr/libexec/git-core/git-switch
rm -f %{buildroot}*/usr/libexec/git-core/git-symbolic-ref
rm -f %{buildroot}*/usr/libexec/git-core/git-tag
rm -f %{buildroot}*/usr/libexec/git-core/git-unpack-file
rm -f %{buildroot}*/usr/libexec/git-core/git-unpack-objects
rm -f %{buildroot}*/usr/libexec/git-core/git-update-index
rm -f %{buildroot}*/usr/libexec/git-core/git-update-ref
rm -f %{buildroot}*/usr/libexec/git-core/git-update-server-info
rm -f %{buildroot}*/usr/libexec/git-core/git-upload-archive
rm -f %{buildroot}*/usr/libexec/git-core/git-upload-pack
rm -f %{buildroot}*/usr/libexec/git-core/git-var
rm -f %{buildroot}*/usr/libexec/git-core/git-verify-commit
rm -f %{buildroot}*/usr/libexec/git-core/git-verify-pack
rm -f %{buildroot}*/usr/libexec/git-core/git-verify-tag
rm -f %{buildroot}*/usr/libexec/git-core/git-version
rm -f %{buildroot}*/usr/libexec/git-core/git-whatchanged
rm -f %{buildroot}*/usr/libexec/git-core/git-worktree
rm -f %{buildroot}*/usr/libexec/git-core/git-write-tree
rm -f %{buildroot}*/usr/libexec/git-core/scalar
rm -f %{buildroot}*/usr/libexec/git-core/git-replay
rm -f %{buildroot}*/usr/libexec/git-core/git-refs
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
