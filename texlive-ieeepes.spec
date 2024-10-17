Name:		texlive-ieeepes
Version:	17359
Release:	2
Summary:	IEEE Power Engineering Society Transactions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ieeepes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeepes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeepes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Supports typesetting of transactions, as well as discussions
and closures, for the IEEE Power Engineering Society
Transactions journals.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ieeepes/ieeepes.bst
%{_texmfdistdir}/tex/latex/ieeepes/ieeepes.sty
%doc %{_texmfdistdir}/doc/latex/ieeepes/README
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_check.bib
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_check.tex
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_doc.pdf
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_doc.tex
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_skel.tex
%doc %{_texmfdistdir}/doc/latex/ieeepes/vk.eps

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
