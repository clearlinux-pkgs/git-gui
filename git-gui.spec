#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : git-gui
Version  : 2.29.2
Release  : 31
URL      : https://www.kernel.org/pub/software/scm/git/git-2.29.2.tar.xz
Source0  : https://www.kernel.org/pub/software/scm/git/git-2.29.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSL-1.0 GPL-2.0 MIT
Requires: git-gui-bin = %{version}-%{release}
Requires: git-gui-data = %{version}-%{release}
Requires: git-gui-libexec = %{version}-%{release}
Requires: git-gui-license = %{version}-%{release}
Requires: git = %{version}
Requires: tk
BuildRequires : asciidoc
BuildRequires : buildreq-cmake
BuildRequires : buildreq-golang
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


%prep
%setup -q -n git-2.29.2
cd %{_builddir}/git-2.29.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604014615
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1604014615
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/git-gui
cp %{_builddir}/git-2.29.2/COPYING %{buildroot}/usr/share/package-licenses/git-gui/3ee0019d4f4ea0a9d3f50800833f30dc14e2968e
cp %{_builddir}/git-2.29.2/compat/nedmalloc/License.txt %{buildroot}/usr/share/package-licenses/git-gui/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/git-2.29.2/contrib/persistent-https/LICENSE %{buildroot}/usr/share/package-licenses/git-gui/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/git-2.29.2/contrib/subtree/COPYING %{buildroot}/usr/share/package-licenses/git-gui/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/git-2.29.2/sha1dc/LICENSE.txt %{buildroot}/usr/share/package-licenses/git-gui/f0197ae0a546d825bcd59ba21034f36272080a4a
cp %{_builddir}/git-2.29.2/t/diff-lib/COPYING %{buildroot}/usr/share/package-licenses/git-gui/2444921d595953ac768e3fb0c8ed97e62a45dc38
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/git
rm -f %{buildroot}/usr/bin/git-receive-pack
rm -f %{buildroot}/usr/bin/git-shell
rm -f %{buildroot}/usr/bin/git-upload-archive
rm -f %{buildroot}/usr/bin/git-upload-pack
rm -f %{buildroot}/usr/bin/haswell/git
rm -f %{buildroot}/usr/bin/haswell/git-receive-pack
rm -f %{buildroot}/usr/bin/haswell/git-shell
rm -f %{buildroot}/usr/bin/haswell/git-upload-archive
rm -f %{buildroot}/usr/bin/haswell/git-upload-pack
rm -f %{buildroot}/usr/share/gitweb/gitweb.cgi
rm -f %{buildroot}/usr/share/perl5/FromCPAN/Error.pm
rm -f %{buildroot}/usr/share/perl5/FromCPAN/Mail/Address.pm
rm -f %{buildroot}/usr/share/perl5/Git.pm
rm -f %{buildroot}/usr/share/perl5/Git/I18N.pm
rm -f %{buildroot}/usr/share/perl5/Git/IndexInfo.pm
rm -f %{buildroot}/usr/share/perl5/Git/LoadCPAN.pm
rm -f %{buildroot}/usr/share/perl5/Git/LoadCPAN/Error.pm
rm -f %{buildroot}/usr/share/perl5/Git/LoadCPAN/Mail/Address.pm
rm -f %{buildroot}/usr/share/perl5/Git/Packet.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Editor.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Fetcher.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/GlobSpec.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Log.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Memoize/YAML.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Migration.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Prompt.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Ra.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Utils.pm
rm -f %{buildroot}/usr/share/bash-completion/completions/git
rm -f %{buildroot}/usr/share/git-core/templates/description
rm -f %{buildroot}/usr/share/git-core/templates/hooks/applypatch-msg.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/commit-msg.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/post-update.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/pre-applypatch.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/pre-commit.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/pre-push.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/pre-receive.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/update.sample
rm -f %{buildroot}/usr/share/git-core/templates/info/exclude
rm -f %{buildroot}/usr/share/gitweb/static/git-favicon.png
rm -f %{buildroot}/usr/share/gitweb/static/git-logo.png
rm -f %{buildroot}/usr/share/gitweb/static/gitweb.css
rm -f %{buildroot}/usr/share/gitweb/static/gitweb.js
rm -f %{buildroot}/usr/bin/git-cvsserver
rm -f %{buildroot}/usr/libexec/git-core/git-add--interactive
rm -f %{buildroot}/usr/libexec/git-core/git-archimport
rm -f %{buildroot}/usr/libexec/git-core/git-cvsexportcommit
rm -f %{buildroot}/usr/libexec/git-core/git-cvsimport
rm -f %{buildroot}/usr/libexec/git-core/git-cvsserver
rm -f %{buildroot}/usr/libexec/git-core/git-instaweb
rm -f %{buildroot}/usr/libexec/git-core/git-p4
rm -f %{buildroot}/usr/libexec/git-core/git-request-pull
rm -f %{buildroot}/usr/libexec/git-core/git-send-email
rm -f %{buildroot}/usr/libexec/git-core/git-svn
rm -f %{buildroot}/usr/share/git-core/templates/hooks/fsmonitor-watchman.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/pre-rebase.sample
rm -f %{buildroot}/usr/share/git-core/templates/hooks/prepare-commit-msg.sample
rm -f %{buildroot}/usr/share/gitweb/gitweb.cgi
rm -f %{buildroot}/usr/share/perl5/FromCPAN/Error.pm
rm -f %{buildroot}/usr/share/perl5/FromCPAN/Mail/Address.pm
rm -f %{buildroot}/usr/share/perl5/Git.pm
rm -f %{buildroot}/usr/share/perl5/Git/I18N.pm
rm -f %{buildroot}/usr/share/perl5/Git/IndexInfo.pm
rm -f %{buildroot}/usr/share/perl5/Git/LoadCPAN.pm
rm -f %{buildroot}/usr/share/perl5/Git/LoadCPAN/Error.pm
rm -f %{buildroot}/usr/share/perl5/Git/LoadCPAN/Mail/Address.pm
rm -f %{buildroot}/usr/share/perl5/Git/Packet.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Editor.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Fetcher.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/GlobSpec.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Log.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Memoize/YAML.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Migration.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Prompt.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Ra.pm
rm -f %{buildroot}/usr/share/perl5/Git/SVN/Utils.pm
rm -f %{buildroot}/usr/libexec/git-core/git-add--interactive
rm -f %{buildroot}/usr/libexec/git-core/git-archimport
rm -f %{buildroot}/usr/libexec/git-core/git-cvsexportcommit
rm -f %{buildroot}/usr/libexec/git-core/git-cvsimport
rm -f %{buildroot}/usr/libexec/git-core/git-cvsserver
rm -f %{buildroot}/usr/libexec/git-core/git-instaweb
rm -f %{buildroot}/usr/libexec/git-core/git-p4
rm -f %{buildroot}/usr/libexec/git-core/git-request-pull
rm -f %{buildroot}/usr/libexec/git-core/git-send-email
rm -f %{buildroot}/usr/libexec/git-core/git-svn
rm -f %{buildroot}/usr/libexec/git-core/git
rm -f %{buildroot}/usr/libexec/git-core/git-add
rm -f %{buildroot}/usr/libexec/git-core/git-am
rm -f %{buildroot}/usr/libexec/git-core/git-annotate
rm -f %{buildroot}/usr/libexec/git-core/git-apply
rm -f %{buildroot}/usr/libexec/git-core/git-archive
rm -f %{buildroot}/usr/libexec/git-core/git-bisect
rm -f %{buildroot}/usr/libexec/git-core/git-bisect--helper
rm -f %{buildroot}/usr/libexec/git-core/git-blame
rm -f %{buildroot}/usr/libexec/git-core/git-branch
rm -f %{buildroot}/usr/libexec/git-core/git-bundle
rm -f %{buildroot}/usr/libexec/git-core/git-cat-file
rm -f %{buildroot}/usr/libexec/git-core/git-check-attr
rm -f %{buildroot}/usr/libexec/git-core/git-check-ignore
rm -f %{buildroot}/usr/libexec/git-core/git-check-mailmap
rm -f %{buildroot}/usr/libexec/git-core/git-check-ref-format
rm -f %{buildroot}/usr/libexec/git-core/git-checkout
rm -f %{buildroot}/usr/libexec/git-core/git-checkout-index
rm -f %{buildroot}/usr/libexec/git-core/git-cherry
rm -f %{buildroot}/usr/libexec/git-core/git-cherry-pick
rm -f %{buildroot}/usr/libexec/git-core/git-citool
rm -f %{buildroot}/usr/libexec/git-core/git-clean
rm -f %{buildroot}/usr/libexec/git-core/git-clone
rm -f %{buildroot}/usr/libexec/git-core/git-column
rm -f %{buildroot}/usr/libexec/git-core/git-commit
rm -f %{buildroot}/usr/libexec/git-core/git-commit-graph
rm -f %{buildroot}/usr/libexec/git-core/git-commit-tree
rm -f %{buildroot}/usr/libexec/git-core/git-config
rm -f %{buildroot}/usr/libexec/git-core/git-count-objects
rm -f %{buildroot}/usr/libexec/git-core/git-credential
rm -f %{buildroot}/usr/libexec/git-core/git-credential-cache
rm -f %{buildroot}/usr/libexec/git-core/git-credential-cache--daemon
rm -f %{buildroot}/usr/libexec/git-core/git-credential-store
rm -f %{buildroot}/usr/libexec/git-core/git-daemon
rm -f %{buildroot}/usr/libexec/git-core/git-describe
rm -f %{buildroot}/usr/libexec/git-core/git-diff
rm -f %{buildroot}/usr/libexec/git-core/git-diff-files
rm -f %{buildroot}/usr/libexec/git-core/git-diff-index
rm -f %{buildroot}/usr/libexec/git-core/git-diff-tree
rm -f %{buildroot}/usr/libexec/git-core/git-difftool
rm -f %{buildroot}/usr/libexec/git-core/git-difftool--helper
rm -f %{buildroot}/usr/libexec/git-core/git-fast-export
rm -f %{buildroot}/usr/libexec/git-core/git-fast-import
rm -f %{buildroot}/usr/libexec/git-core/git-fetch
rm -f %{buildroot}/usr/libexec/git-core/git-fetch-pack
rm -f %{buildroot}/usr/libexec/git-core/git-filter-branch
rm -f %{buildroot}/usr/libexec/git-core/git-fmt-merge-msg
rm -f %{buildroot}/usr/libexec/git-core/git-for-each-ref
rm -f %{buildroot}/usr/libexec/git-core/git-format-patch
rm -f %{buildroot}/usr/libexec/git-core/git-fsck
rm -f %{buildroot}/usr/libexec/git-core/git-fsck-objects
rm -f %{buildroot}/usr/libexec/git-core/git-gc
rm -f %{buildroot}/usr/libexec/git-core/git-get-tar-commit-id
rm -f %{buildroot}/usr/libexec/git-core/git-grep
rm -f %{buildroot}/usr/libexec/git-core/git-hash-object
rm -f %{buildroot}/usr/libexec/git-core/git-help
rm -f %{buildroot}/usr/libexec/git-core/git-http-backend
rm -f %{buildroot}/usr/libexec/git-core/git-http-fetch
rm -f %{buildroot}/usr/libexec/git-core/git-http-push
rm -f %{buildroot}/usr/libexec/git-core/git-imap-send
rm -f %{buildroot}/usr/libexec/git-core/git-index-pack
rm -f %{buildroot}/usr/libexec/git-core/git-init
rm -f %{buildroot}/usr/libexec/git-core/git-init-db
rm -f %{buildroot}/usr/libexec/git-core/git-interpret-trailers
rm -f %{buildroot}/usr/libexec/git-core/git-legacy-rebase
rm -f %{buildroot}/usr/libexec/git-core/git-log
rm -f %{buildroot}/usr/libexec/git-core/git-ls-files
rm -f %{buildroot}/usr/libexec/git-core/git-ls-remote
rm -f %{buildroot}/usr/libexec/git-core/git-ls-tree
rm -f %{buildroot}/usr/libexec/git-core/git-mailinfo
rm -f %{buildroot}/usr/libexec/git-core/git-mailsplit
rm -f %{buildroot}/usr/libexec/git-core/git-merge
rm -f %{buildroot}/usr/libexec/git-core/git-merge-base
rm -f %{buildroot}/usr/libexec/git-core/git-merge-file
rm -f %{buildroot}/usr/libexec/git-core/git-merge-index
rm -f %{buildroot}/usr/libexec/git-core/git-merge-octopus
rm -f %{buildroot}/usr/libexec/git-core/git-merge-one-file
rm -f %{buildroot}/usr/libexec/git-core/git-merge-ours
rm -f %{buildroot}/usr/libexec/git-core/git-merge-recursive
rm -f %{buildroot}/usr/libexec/git-core/git-merge-resolve
rm -f %{buildroot}/usr/libexec/git-core/git-merge-subtree
rm -f %{buildroot}/usr/libexec/git-core/git-merge-tree
rm -f %{buildroot}/usr/libexec/git-core/git-mergetool
rm -f %{buildroot}/usr/libexec/git-core/git-mergetool--lib
rm -f %{buildroot}/usr/libexec/git-core/git-mktag
rm -f %{buildroot}/usr/libexec/git-core/git-mktree
rm -f %{buildroot}/usr/libexec/git-core/git-multi-pack-index
rm -f %{buildroot}/usr/libexec/git-core/git-mv
rm -f %{buildroot}/usr/libexec/git-core/git-name-rev
rm -f %{buildroot}/usr/libexec/git-core/git-notes
rm -f %{buildroot}/usr/libexec/git-core/git-pack-objects
rm -f %{buildroot}/usr/libexec/git-core/git-pack-redundant
rm -f %{buildroot}/usr/libexec/git-core/git-pack-refs
rm -f %{buildroot}/usr/libexec/git-core/git-parse-remote
rm -f %{buildroot}/usr/libexec/git-core/git-patch-id
rm -f %{buildroot}/usr/libexec/git-core/git-prune
rm -f %{buildroot}/usr/libexec/git-core/git-prune-packed
rm -f %{buildroot}/usr/libexec/git-core/git-pull
rm -f %{buildroot}/usr/libexec/git-core/git-push
rm -f %{buildroot}/usr/libexec/git-core/git-quiltimport
rm -f %{buildroot}/usr/libexec/git-core/git-range-diff
rm -f %{buildroot}/usr/libexec/git-core/git-read-tree
rm -f %{buildroot}/usr/libexec/git-core/git-rebase
rm -f %{buildroot}/usr/libexec/git-core/git-rebase--am
rm -f %{buildroot}/usr/libexec/git-core/git-rebase--common
rm -f %{buildroot}/usr/libexec/git-core/git-rebase--interactive
rm -f %{buildroot}/usr/libexec/git-core/git-rebase--merge
rm -f %{buildroot}/usr/libexec/git-core/git-rebase--preserve-merges
rm -f %{buildroot}/usr/libexec/git-core/git-receive-pack
rm -f %{buildroot}/usr/libexec/git-core/git-reflog
rm -f %{buildroot}/usr/libexec/git-core/git-remote
rm -f %{buildroot}/usr/libexec/git-core/git-remote-ext
rm -f %{buildroot}/usr/libexec/git-core/git-remote-fd
rm -f %{buildroot}/usr/libexec/git-core/git-remote-ftp
rm -f %{buildroot}/usr/libexec/git-core/git-remote-ftps
rm -f %{buildroot}/usr/libexec/git-core/git-remote-http
rm -f %{buildroot}/usr/libexec/git-core/git-remote-https
rm -f %{buildroot}/usr/libexec/git-core/git-remote-testsvn
rm -f %{buildroot}/usr/libexec/git-core/git-repack
rm -f %{buildroot}/usr/libexec/git-core/git-replace
rm -f %{buildroot}/usr/libexec/git-core/git-rerere
rm -f %{buildroot}/usr/libexec/git-core/git-reset
rm -f %{buildroot}/usr/libexec/git-core/git-rev-list
rm -f %{buildroot}/usr/libexec/git-core/git-rev-parse
rm -f %{buildroot}/usr/libexec/git-core/git-revert
rm -f %{buildroot}/usr/libexec/git-core/git-rm
rm -f %{buildroot}/usr/libexec/git-core/git-send-pack
rm -f %{buildroot}/usr/libexec/git-core/git-serve
rm -f %{buildroot}/usr/libexec/git-core/git-sh-i18n
rm -f %{buildroot}/usr/libexec/git-core/git-sh-i18n--envsubst
rm -f %{buildroot}/usr/libexec/git-core/git-sh-setup
rm -f %{buildroot}/usr/libexec/git-core/git-shell
rm -f %{buildroot}/usr/libexec/git-core/git-shortlog
rm -f %{buildroot}/usr/libexec/git-core/git-show
rm -f %{buildroot}/usr/libexec/git-core/git-show-branch
rm -f %{buildroot}/usr/libexec/git-core/git-show-index
rm -f %{buildroot}/usr/libexec/git-core/git-show-ref
rm -f %{buildroot}/usr/libexec/git-core/git-stage
rm -f %{buildroot}/usr/libexec/git-core/git-stash
rm -f %{buildroot}/usr/libexec/git-core/git-status
rm -f %{buildroot}/usr/libexec/git-core/git-stripspace
rm -f %{buildroot}/usr/libexec/git-core/git-submodule
rm -f %{buildroot}/usr/libexec/git-core/git-submodule--helper
rm -f %{buildroot}/usr/libexec/git-core/git-symbolic-ref
rm -f %{buildroot}/usr/libexec/git-core/git-tag
rm -f %{buildroot}/usr/libexec/git-core/git-unpack-file
rm -f %{buildroot}/usr/libexec/git-core/git-unpack-objects
rm -f %{buildroot}/usr/libexec/git-core/git-update-index
rm -f %{buildroot}/usr/libexec/git-core/git-update-ref
rm -f %{buildroot}/usr/libexec/git-core/git-update-server-info
rm -f %{buildroot}/usr/libexec/git-core/git-upload-archive
rm -f %{buildroot}/usr/libexec/git-core/git-upload-pack
rm -f %{buildroot}/usr/libexec/git-core/git-var
rm -f %{buildroot}/usr/libexec/git-core/git-verify-commit
rm -f %{buildroot}/usr/libexec/git-core/git-verify-pack
rm -f %{buildroot}/usr/libexec/git-core/git-verify-tag
rm -f %{buildroot}/usr/libexec/git-core/git-web--browse
rm -f %{buildroot}/usr/libexec/git-core/git-whatchanged
rm -f %{buildroot}/usr/libexec/git-core/git-worktree
rm -f %{buildroot}/usr/libexec/git-core/git-write-tree
rm -f %{buildroot}/usr/libexec/git-core/mergetools/araxis
rm -f %{buildroot}/usr/libexec/git-core/mergetools/bc
rm -f %{buildroot}/usr/libexec/git-core/mergetools/bc3
rm -f %{buildroot}/usr/libexec/git-core/mergetools/codecompare
rm -f %{buildroot}/usr/libexec/git-core/mergetools/deltawalker
rm -f %{buildroot}/usr/libexec/git-core/mergetools/diffmerge
rm -f %{buildroot}/usr/libexec/git-core/mergetools/diffuse
rm -f %{buildroot}/usr/libexec/git-core/mergetools/ecmerge
rm -f %{buildroot}/usr/libexec/git-core/mergetools/emerge
rm -f %{buildroot}/usr/libexec/git-core/mergetools/examdiff
rm -f %{buildroot}/usr/libexec/git-core/mergetools/guiffy
rm -f %{buildroot}/usr/libexec/git-core/mergetools/gvimdiff
rm -f %{buildroot}/usr/libexec/git-core/mergetools/gvimdiff2
rm -f %{buildroot}/usr/libexec/git-core/mergetools/gvimdiff3
rm -f %{buildroot}/usr/libexec/git-core/mergetools/kdiff3
rm -f %{buildroot}/usr/libexec/git-core/mergetools/kompare
rm -f %{buildroot}/usr/libexec/git-core/mergetools/meld
rm -f %{buildroot}/usr/libexec/git-core/mergetools/opendiff
rm -f %{buildroot}/usr/libexec/git-core/mergetools/p4merge
rm -f %{buildroot}/usr/libexec/git-core/mergetools/tkdiff
rm -f %{buildroot}/usr/libexec/git-core/mergetools/tortoisemerge
rm -f %{buildroot}/usr/libexec/git-core/mergetools/vimdiff
rm -f %{buildroot}/usr/libexec/git-core/mergetools/vimdiff2
rm -f %{buildroot}/usr/libexec/git-core/mergetools/vimdiff3
rm -f %{buildroot}/usr/libexec/git-core/mergetools/winmerge
rm -f %{buildroot}/usr/libexec/git-core/mergetools/xxdiff
rm -f %{buildroot}/usr/share/man/man1/git-am.1
rm -f %{buildroot}/usr/share/man/man1/git-annotate.1
rm -f %{buildroot}/usr/share/man/man1/git-apply.1
rm -f %{buildroot}/usr/share/man/man1/git-archimport.1
rm -f %{buildroot}/usr/share/man/man1/git-archive.1
rm -f %{buildroot}/usr/share/man/man1/git-bisect.1
rm -f %{buildroot}/usr/share/man/man1/git-blame.1
rm -f %{buildroot}/usr/share/man/man1/git-branch.1
rm -f %{buildroot}/usr/share/man/man1/git-bundle.1
rm -f %{buildroot}/usr/share/man/man1/git-cat-file.1
rm -f %{buildroot}/usr/share/man/man1/git-check-attr.1
rm -f %{buildroot}/usr/share/man/man1/git-check-ignore.1
rm -f %{buildroot}/usr/share/man/man1/git-check-mailmap.1
rm -f %{buildroot}/usr/share/man/man1/git-check-ref-format.1
rm -f %{buildroot}/usr/share/man/man1/git-checkout-index.1
rm -f %{buildroot}/usr/share/man/man1/git-checkout.1
rm -f %{buildroot}/usr/share/man/man1/git-cherry-pick.1
rm -f %{buildroot}/usr/share/man/man1/git-cherry.1
rm -f %{buildroot}/usr/share/man/man1/git-citool.1
rm -f %{buildroot}/usr/share/man/man1/git-clean.1
rm -f %{buildroot}/usr/share/man/man1/git-clone.1
rm -f %{buildroot}/usr/share/man/man1/git-column.1
rm -f %{buildroot}/usr/share/man/man1/git-commit-graph.1
rm -f %{buildroot}/usr/share/man/man1/git-commit-tree.1
rm -f %{buildroot}/usr/share/man/man1/git-commit.1
rm -f %{buildroot}/usr/share/man/man1/git-config.1
rm -f %{buildroot}/usr/share/man/man1/git-count-objects.1
rm -f %{buildroot}/usr/share/man/man1/git-credential-cache--daemon.1
rm -f %{buildroot}/usr/share/man/man1/git-credential-cache.1
rm -f %{buildroot}/usr/share/man/man1/git-credential-store.1
rm -f %{buildroot}/usr/share/man/man1/git-credential.1
rm -f %{buildroot}/usr/share/man/man1/git-cvsexportcommit.1
rm -f %{buildroot}/usr/share/man/man1/git-cvsimport.1
rm -f %{buildroot}/usr/share/man/man1/git-cvsserver.1
rm -f %{buildroot}/usr/share/man/man1/git-daemon.1
rm -f %{buildroot}/usr/share/man/man1/git-describe.1
rm -f %{buildroot}/usr/share/man/man1/git-diff-files.1
rm -f %{buildroot}/usr/share/man/man1/git-diff-index.1
rm -f %{buildroot}/usr/share/man/man1/git-diff-tree.1
rm -f %{buildroot}/usr/share/man/man1/git-diff.1
rm -f %{buildroot}/usr/share/man/man1/git-difftool.1
rm -f %{buildroot}/usr/share/man/man1/git-fast-export.1
rm -f %{buildroot}/usr/share/man/man1/git-fast-import.1
rm -f %{buildroot}/usr/share/man/man1/git-fetch-pack.1
rm -f %{buildroot}/usr/share/man/man1/git-fetch.1
rm -f %{buildroot}/usr/share/man/man1/git-filter-branch.1
rm -f %{buildroot}/usr/share/man/man1/git-fmt-merge-msg.1
rm -f %{buildroot}/usr/share/man/man1/git-for-each-ref.1
rm -f %{buildroot}/usr/share/man/man1/git-format-patch.1
rm -f %{buildroot}/usr/share/man/man1/git-fsck-objects.1
rm -f %{buildroot}/usr/share/man/man1/git-fsck.1
rm -f %{buildroot}/usr/share/man/man1/git-gc.1
rm -f %{buildroot}/usr/share/man/man1/git-get-tar-commit-id.1
rm -f %{buildroot}/usr/share/man/man1/git-grep.1
rm -f %{buildroot}/usr/share/man/man1/git-hash-object.1
rm -f %{buildroot}/usr/share/man/man1/git-help.1
rm -f %{buildroot}/usr/share/man/man1/git-http-backend.1
rm -f %{buildroot}/usr/share/man/man1/git-http-fetch.1
rm -f %{buildroot}/usr/share/man/man1/git-http-push.1
rm -f %{buildroot}/usr/share/man/man1/git-imap-send.1
rm -f %{buildroot}/usr/share/man/man1/git-index-pack.1
rm -f %{buildroot}/usr/share/man/man1/git-init-db.1
rm -f %{buildroot}/usr/share/man/man1/git-init.1
rm -f %{buildroot}/usr/share/man/man1/git-instaweb.1
rm -f %{buildroot}/usr/share/man/man1/git-interpret-trailers.1
rm -f %{buildroot}/usr/share/man/man1/git-log.1
rm -f %{buildroot}/usr/share/man/man1/git-ls-files.1
rm -f %{buildroot}/usr/share/man/man1/git-ls-remote.1
rm -f %{buildroot}/usr/share/man/man1/git-ls-tree.1
rm -f %{buildroot}/usr/share/man/man1/git-mailinfo.1
rm -f %{buildroot}/usr/share/man/man1/git-mailsplit.1
rm -f %{buildroot}/usr/share/man/man1/git-merge-base.1
rm -f %{buildroot}/usr/share/man/man1/git-merge-file.1
rm -f %{buildroot}/usr/share/man/man1/git-merge-index.1
rm -f %{buildroot}/usr/share/man/man1/git-merge-one-file.1
rm -f %{buildroot}/usr/share/man/man1/git-merge-tree.1
rm -f %{buildroot}/usr/share/man/man1/git-merge.1
rm -f %{buildroot}/usr/share/man/man1/git-mergetool--lib.1
rm -f %{buildroot}/usr/share/man/man1/git-mergetool.1
rm -f %{buildroot}/usr/share/man/man1/git-mktag.1
rm -f %{buildroot}/usr/share/man/man1/git-mktree.1
rm -f %{buildroot}/usr/share/man/man1/git-multi-pack-index.1
rm -f %{buildroot}/usr/share/man/man1/git-mv.1
rm -f %{buildroot}/usr/share/man/man1/git-name-rev.1
rm -f %{buildroot}/usr/share/man/man1/git-notes.1
rm -f %{buildroot}/usr/share/man/man1/git-p4.1
rm -f %{buildroot}/usr/share/man/man1/git-pack-objects.1
rm -f %{buildroot}/usr/share/man/man1/git-pack-redundant.1
rm -f %{buildroot}/usr/share/man/man1/git-pack-refs.1
rm -f %{buildroot}/usr/share/man/man1/git-parse-remote.1
rm -f %{buildroot}/usr/share/man/man1/git-patch-id.1
rm -f %{buildroot}/usr/share/man/man1/git-prune-packed.1
rm -f %{buildroot}/usr/share/man/man1/git-prune.1
rm -f %{buildroot}/usr/share/man/man1/git-pull.1
rm -f %{buildroot}/usr/share/man/man1/git-push.1
rm -f %{buildroot}/usr/share/man/man1/git-quiltimport.1
rm -f %{buildroot}/usr/share/man/man1/git-range-diff.1
rm -f %{buildroot}/usr/share/man/man1/git-read-tree.1
rm -f %{buildroot}/usr/share/man/man1/git-rebase.1
rm -f %{buildroot}/usr/share/man/man1/git-receive-pack.1
rm -f %{buildroot}/usr/share/man/man1/git-reflog.1
rm -f %{buildroot}/usr/share/man/man1/git-remote-ext.1
rm -f %{buildroot}/usr/share/man/man1/git-remote-fd.1
rm -f %{buildroot}/usr/share/man/man1/git-remote-testgit.1
rm -f %{buildroot}/usr/share/man/man1/git-remote.1
rm -f %{buildroot}/usr/share/man/man1/git-repack.1
rm -f %{buildroot}/usr/share/man/man1/git-replace.1
rm -f %{buildroot}/usr/share/man/man1/git-request-pull.1
rm -f %{buildroot}/usr/share/man/man1/git-rerere.1
rm -f %{buildroot}/usr/share/man/man1/git-reset.1
rm -f %{buildroot}/usr/share/man/man1/git-rev-list.1
rm -f %{buildroot}/usr/share/man/man1/git-rev-parse.1
rm -f %{buildroot}/usr/share/man/man1/git-revert.1
rm -f %{buildroot}/usr/share/man/man1/git-rm.1
rm -f %{buildroot}/usr/share/man/man1/git-send-email.1
rm -f %{buildroot}/usr/share/man/man1/git-send-pack.1
rm -f %{buildroot}/usr/share/man/man1/git-sh-i18n--envsubst.1
rm -f %{buildroot}/usr/share/man/man1/git-sh-i18n.1
rm -f %{buildroot}/usr/share/man/man1/git-sh-setup.1
rm -f %{buildroot}/usr/share/man/man1/git-shell.1
rm -f %{buildroot}/usr/share/man/man1/git-shortlog.1
rm -f %{buildroot}/usr/share/man/man1/git-show-branch.1
rm -f %{buildroot}/usr/share/man/man1/git-show-index.1
rm -f %{buildroot}/usr/share/man/man1/git-show-ref.1
rm -f %{buildroot}/usr/share/man/man1/git-show.1
rm -f %{buildroot}/usr/share/man/man1/git-stage.1
rm -f %{buildroot}/usr/share/man/man1/git-stash.1
rm -f %{buildroot}/usr/share/man/man1/git-status.1
rm -f %{buildroot}/usr/share/man/man1/git-stripspace.1
rm -f %{buildroot}/usr/share/man/man1/git-submodule.1
rm -f %{buildroot}/usr/share/man/man1/git-svn.1
rm -f %{buildroot}/usr/share/man/man1/git-symbolic-ref.1
rm -f %{buildroot}/usr/share/man/man1/git-tag.1
rm -f %{buildroot}/usr/share/man/man1/git-unpack-file.1
rm -f %{buildroot}/usr/share/man/man1/git-unpack-objects.1
rm -f %{buildroot}/usr/share/man/man1/git-update-index.1
rm -f %{buildroot}/usr/share/man/man1/git-update-ref.1
rm -f %{buildroot}/usr/share/man/man1/git-update-server-info.1
rm -f %{buildroot}/usr/share/man/man1/git-upload-archive.1
rm -f %{buildroot}/usr/share/man/man1/git-upload-pack.1
rm -f %{buildroot}/usr/share/man/man1/git-var.1
rm -f %{buildroot}/usr/share/man/man1/git-verify-commit.1
rm -f %{buildroot}/usr/share/man/man1/git-verify-pack.1
rm -f %{buildroot}/usr/share/man/man1/git-verify-tag.1
rm -f %{buildroot}/usr/share/man/man1/git-web--browse.1
rm -f %{buildroot}/usr/share/man/man1/git-whatchanged.1
rm -f %{buildroot}/usr/share/man/man1/git-worktree.1
rm -f %{buildroot}/usr/share/man/man1/git-write-tree.1
rm -f %{buildroot}/usr/share/man/man1/git.1
rm -f %{buildroot}/usr/share/man/man1/gitremote-helpers.1
rm -f %{buildroot}/usr/share/man/man1/gitweb.1
rm -f %{buildroot}/usr/share/man/man5/gitattributes.5
rm -f %{buildroot}/usr/share/man/man5/githooks.5
rm -f %{buildroot}/usr/share/man/man5/gitignore.5
rm -f %{buildroot}/usr/share/man/man5/gitmodules.5
rm -f %{buildroot}/usr/share/man/man5/gitrepository-layout.5
rm -f %{buildroot}/usr/share/man/man5/gitweb.conf.5
rm -f %{buildroot}/usr/share/man/man7/gitcli.7
rm -f %{buildroot}/usr/share/man/man7/gitcore-tutorial.7
rm -f %{buildroot}/usr/share/man/man7/gitcredentials.7
rm -f %{buildroot}/usr/share/man/man7/gitcvs-migration.7
rm -f %{buildroot}/usr/share/man/man7/gitdiffcore.7
rm -f %{buildroot}/usr/share/man/man7/giteveryday.7
rm -f %{buildroot}/usr/share/man/man7/gitglossary.7
rm -f %{buildroot}/usr/share/man/man7/gitnamespaces.7
rm -f %{buildroot}/usr/share/man/man7/gitrevisions.7
rm -f %{buildroot}/usr/share/man/man7/gitsubmodules.7
rm -f %{buildroot}/usr/share/man/man7/gittutorial-2.7
rm -f %{buildroot}/usr/share/man/man7/gittutorial.7
rm -f %{buildroot}/usr/share/man/man7/gitworkflows.7
rm -f %{buildroot}/usr/lib/perl5/site_perl/5.*/x86_64-linux-thread-multi/auto/Git/.packlist
rm -f %{buildroot}/usr/libexec/git-core/git-legacy-stash
rm -f %{buildroot}/usr/libexec/git-core/mergetools/smerge
rm -f %{buildroot}/usr/libexec/git-core/git-switch
rm -f %{buildroot}/usr/libexec/git-core/git-restore
rm -f %{buildroot}/usr/libexec/git-core/git-env--helper
rm -f %{buildroot}/usr/libexec/git-core/git-sparse-checkout
rm -f %{buildroot}/usr/share/git-core/templates/hooks/pre-merge-commit.sample
rm -f %{buildroot}/usr/libexec/git-core/git-bugreport
rm -f %{buildroot}/usr/libexec/git-core/mergetools/nvimdiff
## install_append content
rm -rf %{buildroot}/usr/share/locale
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
/usr/share/package-licenses/git-gui/2444921d595953ac768e3fb0c8ed97e62a45dc38
/usr/share/package-licenses/git-gui/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/git-gui/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/git-gui/3ee0019d4f4ea0a9d3f50800833f30dc14e2968e
/usr/share/package-licenses/git-gui/f0197ae0a546d825bcd59ba21034f36272080a4a
