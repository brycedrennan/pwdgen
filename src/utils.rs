use rand::{distributions::Uniform, Rng};

static PASSPHRASE_LIST: &str = include_str!("wordlist_1830_match6.txt");

fn get_passphrase_list() -> Vec<&'static str> {
    PASSPHRASE_LIST.lines().collect()
}

// Function to generate a vector of emoji characters from the specified groups
fn emoji_chars_from_groups() -> Vec<char> {
    let mut emojis = Vec::new();
    emojis.extend(
        emojis::Group::FoodAndDrink
            .emojis()
            .map(|e| e.as_str().chars().next().unwrap()),
    );
    emojis.extend(
        emojis::Group::AnimalsAndNature
            .emojis()
            .map(|e| e.as_str().chars().next().unwrap()),
    );
    emojis.extend(
        emojis::Group::Objects
            .emojis()
            .map(|e| e.as_str().chars().next().unwrap()),
    );
    emojis
}

pub fn generate_password(length: usize, password_type: &str) -> String {
    let mut rng = rand::thread_rng();

    // Define the character sets for each password type
    let ascii_chars = (' '..='~').collect::<Vec<char>>(); // ASCII characters from space to tilde
    let alphanumeric_chars = ('0'..='9')
        .chain('a'..='z')
        .chain('A'..='Z')
        .collect::<Vec<char>>();
    let numeric_chars = ('0'..='9').collect::<Vec<char>>();
    let emoji_chars = emoji_chars_from_groups();
    let passphrase_words = get_passphrase_list();

    // Create a password based on the specified type
    match password_type {
        "ascii" => (0..length)
            .map(|_| ascii_chars[rng.gen_range(0..ascii_chars.len())])
            .collect(),
        "alphanumeric" => (0..length)
            .map(|_| alphanumeric_chars[rng.gen_range(0..alphanumeric_chars.len())])
            .collect(),
        "numeric" => (0..length)
            .map(|_| numeric_chars[rng.gen_range(0..numeric_chars.len())])
            .collect(),
        "emoji" => (0..length)
            .map(|_| emoji_chars[rng.gen_range(0..emoji_chars.len())])
            .collect(),
        "passphrase" => (0..length)
            .map(|_| passphrase_words[rng.gen_range(0..passphrase_words.len())].to_string())
            .collect::<Vec<_>>()
            .join("-"),
        "password" => {
            // Combination of ascii and emoji
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_passphrase_list() {
        let passphrases = get_passphrase_list();

        assert!(
            passphrases.contains(&"elephant"),
            "The passphrase list should contain 'known_word'."
        );

        let expected_length = 121932; // Update this with the actual expected length
        assert_eq!(
            passphrases.len(),
            expected_length,
            "The passphrase list should contain {} words.",
            expected_length
        );
    }
}
