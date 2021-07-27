import 'dart:io';

main() {
  stdout.writeln("Entre ton age :");
  var age = stdin.readLineSync();
  if (age == "18") {
    print("Tu es majeur $age");
  } else {
    print("Tu es mineur $age");
  }
}
