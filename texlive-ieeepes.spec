# revision 17359
# category Package
# catalog-ctan /macros/latex/contrib/ieeepes
# catalog-date 2010-03-06 17:23:09 +0100
# catalog-license lppl
# catalog-version 4.0
Name:		texlive-ieeepes
Version:	4.0
Release:	7
Summary:	IEEE Power Engineering Society Transactions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ieeepes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeepes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeepes.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.0-2
+ Revision: 752687
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.0-1
+ Revision: 718695
- texlive-ieeepes
- texlive-ieeepes
- texlive-ieeepes
- texlive-ieeepes

