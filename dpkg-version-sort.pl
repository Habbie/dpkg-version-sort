#!/usr/bin/perl
sub dpkgcomp
{
  return 1 if(system("dpkg --compare-versions $a lt $b"));
  return -1 if(system("dpkg --compare-versions $a gt $b"));
  return 0;
}
@l = <>;
chomp(@l);
@s = sort dpkgcomp @l;
print join("\n", @s), "\n";
