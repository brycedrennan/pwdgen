use clap::{App, Arg};
use rand::{distributions::Uniform, Rng};

static PASSPHRASE_LIST: &str = include_str!("wordlist.txt");

fn get_passphrase_list() -> Vec<&'static str> {
    PASSPHRASE_LIST.lines().collect()
}



// Function to generate a vector of emoji characters from the specified groups
fn emoji_chars_from_groups() -> Vec<char> {
    let mut emojis = Vec::new();
    emojis.extend(emojis::Group::FoodAndDrink.emojis().map(|e| e.as_str().chars().next().unwrap()));
    emojis.extend(emojis::Group::AnimalsAndNature.emojis().map(|e| e.as_str().chars().next().unwrap()));
    emojis.extend(emojis::Group::Objects.emojis().map(|e| e.as_str().chars().next().unwrap()));
    emojis
}


fn generate_password(length: usize, password_type: &str) -> String {
    let mut rng = rand::thread_rng();

    // Define the character sets for each password type
    let ascii_chars = (' '..='~').collect::<Vec<char>>(); // ASCII characters from space to tilde
    let alphanumeric_chars = ('0'..='9').chain('a'..='z').chain('A'..='Z').collect::<Vec<char>>();
    let numeric_chars = ('0'..='9').collect::<Vec<char>>();
    let emoji_chars = emoji_chars_from_groups();
    let passphrase_words = get_passphrase_list();

    // Create a password based on the specified type
    match password_type {
        "ascii" => (0..length).map(|_| ascii_chars[rng.gen_range(0..ascii_chars.len())]).collect(),
        "alphanumeric" => (0..length).map(|_| alphanumeric_chars[rng.gen_range(0..alphanumeric_chars.len())]).collect(),
        "numeric" => (0..length).map(|_| numeric_chars[rng.gen_range(0..numeric_chars.len())]).collect(),
        "emoji" => (0..length).map(|_| emoji_chars[rng.gen_range(0..emoji_chars.len())]).collect(),
        "passphrase" => (0..length).map(|_| passphrase_words[rng.gen_range(0..passphrase_words.len())].to_string()).collect::<Vec<_>>().join("-"),
        "password" => { // Combination of ascii and emoji
            let mut pass = String::new();
            let ascii_and_emoji = ascii_chars.iter().chain(emoji_chars.iter());
            let dist = Uniform::from(0..ascii_and_emoji.clone().count());
            for _ in 0..length {
                pass.push(*ascii_and_emoji.clone().nth(rng.sample(dist)).unwrap());
            }
            pass
        }
        _ => String::from("Invalid type"), // In case of an invalid type
    }
}

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
            .required(false)) // not required because we will provide a default based on the type
        .get_matches();

    // Use the provided length or default if not provided
    let length = matches.value_of("length")
        .map(|s| s.parse::<usize>().expect("Length must be a number"))
        .unwrap_or(50); // Set a general default length if not provided

    // Process each password type provided in the command line
    if let Some(types) = matches.values_of("type") {
        for password_type in types {
            let specific_length = if password_type == "passphrase" { 6 } else { length };
            let password = generate_password(specific_length, password_type);
            println!("{}", password);
        }
    }
}

