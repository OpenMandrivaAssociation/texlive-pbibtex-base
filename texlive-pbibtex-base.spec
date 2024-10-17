Name:		texlive-pbibtex-base
Version:	61914
Release:	2
Summary:	Bibliography styles and miscellaneous files for pBibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pbibtex-base
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbibtex-base.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbibtex-base.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These are miscellaneous files, including bibliography styles
(.bst), for pBibTeX, which is a Japanese extended version of
BibTeX contained in TeX Live. The bundle is a redistribution
derived from the ptex-texmf distribution by ASCII MEDIA WORKS.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/pbibtex
%{_texmfdistdir}/pbibtex/bst
%{_texmfdistdir}/pbibtex/bst/tipsj.bst
%{_texmfdistdir}/pbibtex/bst/tieice.bst
%{_texmfdistdir}/pbibtex/bst/junsrt.bst
%{_texmfdistdir}/pbibtex/bst/jplain.bst
%{_texmfdistdir}/pbibtex/bst/jorsj.bst
%{_texmfdistdir}/pbibtex/bst/jname.bst
%{_texmfdistdir}/pbibtex/bst/jipsj.bst
%{_texmfdistdir}/pbibtex/bst/jalpha.bst
%{_texmfdistdir}/pbibtex/bst/jabbrv.bst
%{_texmfdistdir}/pbibtex/bib
%{_texmfdistdir}/pbibtex/bib/jxampl.bib
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/ptex
%doc %{_texmfdistdir}/doc/ptex/pbibtex
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxdoc.bib
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxbst.doc
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbibtex.bib
%doc %{_texmfdistdir}/doc/ptex/pbibtex/generate.sh
%doc %{_texmfdistdir}/doc/ptex/pbibtex/cpp.awk
%doc %{_texmfdistdir}/doc/ptex/pbibtex/README.md
%doc %{_texmfdistdir}/doc/ptex/pbibtex/LICENSE

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
