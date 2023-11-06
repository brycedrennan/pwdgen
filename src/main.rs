use clap::{App, Arg};

mod utils;
use utils::generate_password;

fn main() {
    let matches = App::new("Password Generator")
        .version("1.0")
        .author("Your Name")
        .about("Generates a random password")
        .arg(Arg::new("type")
            .short('t')
            .long("type")
            .value_name("TYPE")
            .help("Sets the types of the passwords to generate: ascii, alphanumeric, emoji, numeric, passphrase, password")
            .takes_value(true)
            .multiple_values(true)
            .default_values(&["ascii", "alphanumeric", "emoji", "numeric", "passphrase", "password"]))
        .arg(Arg::new("length")
            .short('l')
            .long("length")
            .value_name("LENGTH")
            .help("Sets the length of the password")
            .takes_value(true)
            .required(false))
        .get_matches();

    let length = matches
        .value_of("length")
        .map(|s| s.parse::<usize>().expect("Length must be a number"))
        .unwrap_or(50); // Set a general default length if not provided

    if let Some(types) = matches.values_of("type") {
        for password_type in types {
            let specific_length = if password_type == "passphrase" {
                6
            } else {
                length
            };
            let password = generate_password(specific_length, password_type);
            println!("{}", password);
        }
    }
}
