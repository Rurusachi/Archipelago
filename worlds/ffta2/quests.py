from typing import NamedTuple, List

questNames = [
    "-",
    "Stranger in the Woods",
    "A Paw Full of Feathers",
    "The Yellow Wings",
    "You Say Tomato",
    "Wanted: Ugohr",
    "Wanted: Gilmunto",
    "Now That's a Fire!",
    "Pearls in the Deep",
    "Mountain Watch",
    "Grounded!",
    "Rumors Abound",
    "Sleepless Nights",
    "Making Music",
    "Making Music part 2",
    "Seeking the Stone",
    "Wanted: Sky Pirate Vaan",
    "A Request",
    "The Rift",
    "The Dig",
    "Through Another's Eyes",
    "Pirate Problems",
    "The Ritual",
    "The Two Grimoires",
    "From the Rift",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "The Search",
    "Gifted",
    "An Elegant Encounter",
    "Where Could He Be?",
    "A Moment's Respite",
    "I've Been Had, Kupo!",
    "A Refined Recruit",
    "I'm Back, Kupo!",
    "Wanted: Friends, Kupo!",
    "-",
    "-",
    "-",
    "A Lost Companion",
    "Help!",
    "Woman of the Wood",
    "The Beast of Aisenfield",
    "Shrine of the Paling Gods",
    "Bringer of Doom",
    "Unplumbed Depths",
    "A Dashing Duel",
    "-",
    "-",
    "Brightmoon Tor",
    "Brightmoon Tor, 2nd Ascent",
    "Brightmoon Tor, 3rd Ascent",
    "-",
    "-",
    "Clan Mates",
    "Reagent Run",
    "To Be a Fighter",
    "The Eastwatch",
    "Kyrra, Dragoon",
    "Banbanga!",
    "The Bangaa Brotherhood",
    "Sleight of Hand",
    "Knowing the Beast",
    "The Nu Mou Nobles",
    "Treasured Tomes",
    "Veis, Assassin",
    "Green Dominion",
    "To Be a Spellblade",
    "The Goug Consortium",
    "Of Kupos and Cannons",
    "Popocho's Chocobos",
    "Popocho's Chocobos part 2",
    "Popocho's Chocobos part 3",
    "A Lanista's Pride",
    "Lord Grayrl!",
    "Instrument of Inspiration",
    "Ravager",
    "Geomancer's Way 8F Sun",
    "Geomancer's Way 8F Rain",
    "Geomancer's Way 8F Snow",
    "Geomancer's Way 8F Mist",
    "General Training I",
    "General Training II",
    "Negotiation I",
    "Negotiation II",
    "Aptitude I",
    "Aptitude II",
    "Teamwork I",
    "Teamwork II",
    "Adaptability I",
    "Adaptability II",
    "Negotiation-Teamwork",
    "Adaptability-Negotiation",
    "Teamwork-Aptitude",
    "Aptitude-Adaptability",
    "Bonga Bugle 8E Blackfrost",
    "Bonga Bugle 8E Skyfrost",
    "Bonga Bugle 8E Skyfrost part 2",
    "Bonga Bugle 8E Skyfrost part 3",
    "Bonga Bugle 8E Greenfire",
    "Bonga Bugle 8E Greenfire part 2",
    "Bonga Bugle 8E Greenfire part 3",
    "Bonga Bugle 8E Greenfire part 4",
    "Bonga Bugle 8E Bloodfire",
    "Bonga Bugle 8E Rosefire",
    "Bonga Bugle 8E Coppersun",
    "Bonga Bugle 8E Coppersun part 2",
    "Bonga Bugle 8E Coppersun part 3",
    "Bonga Bugle 8E Silversun",
    "Bonga Bugle 8E Goldsun",
    "Bonga Bugle 8E Ashleaf",
    "Bonga Bugle 8E Mistleaf",
    "Bonga Bugle 8E Emberleaf",
    "Bonga Bugle 8E Emberleaf part 2",
    "Bonga Bugle 8E Emberleaf part 3",
    "Bonga Bugle 8E Emberleaf part 4",
    "Bonga Bugle 8E Plumfrost",
    "Bonga Bugle 8E Plumfrost part 2",
    "Bonga Bugle 8E Plumfrost part 3",
    "Wanted: The Cyanwolf",
    "Wanted: Lang Bros.",
    "Wanted: Big Eyes",
    "Wanted: The Mirage Bunny",
    "Wanted: Florah",
    "Wanted: Tonberrion",
    "Wanted: Gaitsnipe",
    "Wanted: Icicle Ark",
    "Wanted: Floraxion",
    "Wanted: Moogle Rangers",
    "Wanted: The Mutadragons",
    "Wanted: Magick Weapon",
    "Camoa Cup",
    "Camoa Cup part 2",
    "Camoa Cup part 3",
    "Graszton Cup",
    "Graszton Cup part 2",
    "Graszton Cup part 3",
    "Moorabella Cup",
    "Moorabella Cup part 2",
    "Moorabella Cup part 3",
    "Fluorgis Cup",
    "Fluorgis Cup part 2",
    "Fluorgis Cup part 3",
    "Goug Cup",
    "Goug Cup part 2",
    "Goug Cup part 3",
    "Loar Cup",
    "Loar Cup part 2",
    "Loar Cup part 3",
    "Loar Cup part 4",
    "Loar Cup part 5",
    "Ordalia Cup",
    "Ordalia Cup part 2",
    "Ordalia Cup part 3",
    "Ordalia Cup part 4",
    "Ordalia Cup part 5",
    "Jylland Cup",
    "Jylland Cup part 2",
    "Jylland Cup part 3",
    "Jylland Cup part 4",
    "Jylland Cup part 5",
    "Jylland Cup part 6",
    "Jylland Cup part 7",
    "Champions' Cup",
    "Beetle in a Haystack",
    "Wayward Drake",
    "The White of Its Eye",
    "Flown the Coop",
    "It's a Secret to Everybody",
    "Hellhound Astray",
    "My Little Carrot",
    "Bug Hunt",
    "Bug Hunt part 2",
    "Bug Hunt part 3",
    "A Treasured Heirloom",
    "The Finest Blade",
    "Rancher's Request 8F Yellow",
    "Sun-ripened Mayhem",
    "The Witch of the Fens",
    "Seeding the Harvest",
    "Kupoppy Flower",
    "Maintaining the Balance",
    "The Natural Order",
    "The First Step",
    "The Next Step",
    "The Next Step part 2",
    "A Step Further",
    "The Last Step",
    "Starstruck",
    "Under the Weather",
    "A Chill in the Night",
    "Hunted",
    "Past Burdens",
    "Rude Awakening",
    "Drowsy Draught",
    "Inspiration or Perspiration?",
    "For My Love",
    "My Secret Shame",
    "The Honorable Thing",
    "Shipping Out",
    "Shipping Out part 2",
    "Prepared with Love",
    "Prepared with Love part 2",
    "Meeting the Quota",
    "The Perfect Gift",
    "The Show's Not Over...",
    "A Lady's Proposition",
    "Vim, Vigor, and Go",
    "The Cat's Meow",
    "Cake: The Recipe",
    "Cake: The Ingredients",
    "Cake: The Catastrophe",
    "A Lady's Persistence",
    "Hors D'oeuvre of the Hour",
    "Devilish Delight",
    "Shelling Out",
    "Flantastic Finish",
    "The Art of Gastronomy",
    "The Trappings of Failure",
    "Watching the Watchers",
    "Training Wanted",
    "Time to Act",
    "Wish Upon A Star",
    "Plea for Help",
    "Wall of Flame",
    "The Bangaa of the Rupies",
    "The Nu Mou of the Rupies",
    "The Rivalry of the Rupies",
    "A Bride for Montblanc",
    "An Earnest Search",
    "An Earnest Quandary",
    "An Earnest Quandary part 2",
    "An Earnest Multitude",
    "An Earnest Multitude part 2",
    "An Earnest Multitude part 3",
    "An Earnest Delight",
    "An Earnest Delight part 2",
    "An Earnest Delight part 3",
    "An Earnest Delight part 4",
    "Gripped by Fear",
    "I Must Have It!",
    "It's the Thought",
    "'Cross the Sea",
    "'Cross the Sea part 2",
    "Love-struck",
    "All Good Things...",
    "Stuck in the Muck",
    "One Red Phial",
    "'Tis the Season",
    "Unfamiliar Folk",
    "Duelhorn",
    "Making Port",
    "Foodstuffs: Texture",
    "Foodstuffs: Aroma",
    "Foodstuffs: Appearance",
    "Foodstuffs: Nutrition",
    "Foodstuffs: Bon Appetit",
    "The Way of the Meek",
    "What Was Lost",
    "The Way of the Timid",
    "Great Land Festival",
    "It's a Trap!",
    "Throw Down",
    "I Got a Bad Feeling",
    "Showdown",
    "Red King of Cinquleur",
    "Black King of Cinquleur",
    "Green King of Cinquleur",
    "Blue King of Cinquleur",
    "White King of Cinquleur",
    "The Five Kings",
    "Wanted: Sidekick",
    "The Wonders of Loar",
    "The Wonders of Loar part 2",
    "The Wonders of Loar part 3",
    "The Wonders of Loar part 4",
    "The Camoa Nightwatch",
    "Memories Forged",
    "The Lands of Loar",
    "The Lands of Loar part 2",
    "The Lands of Loar part 3",
    "The Forests of Loar",
    "The Forests of Loar part 2",
    "The Forests of Loar part 3",
    "The Towns of Loar",
    "The Towns of Loar part 2",
    "The Towns of Loar part 3",
    "The Seas of Ordalia",
    "The Seas of Ordalia part 2",
    "The Seas of Ordalia part 3",
    "The Forgotten Places",
    "The Forgotten Places part 2",
    "The Forgotten Places part 3",
    "The Forgotten Places part 4",
    "Bonga Bugle 8E Skyfrost part 4",
    "Bonga Bugle 8E Greenfire part 5",
    "Bonga Bugle 8E Coppersun part 4",
    "Bonga Bugle 8E Emberleaf part 5",
    "Bonga Bugle 8E Plumfrost part 4",
    "The Wonders of Ordalia",
    "The Wonders of Ordalia part 2",
    "The Wonders of Ordalia part 3",
    "For the Cause",
    "On the Rampage",
    "Monster Poaching",
    "Poachers Spotted",
    "An Unseen Foe",
    "Memories",
    "Abducted!",
    "Graszton Nightwatch",
    "Chita on Weapons8ENovices",
    "Chita on Weapons8EAdepts",
    "Chita on Weapons8EMasters",
    "Cilawa the Gluttonous",
    "Escort Wanted",
    "Hunting Season",
    "Moorabella Nightwatch",
    "Fluorgis Nightwatch",
    "Goug Nightwatch",
    "Shady Dealings",
    "Drawn Bridge",
    "A Harvest Hand",
    "Speed Battle, Kupo!",
    "The Genuine Article",
    "The Root of the Problem",
    "The Whole Truth",
    "Wanted: Musician!",
    "A Charm for Luck",
    "A Charm for Luck part 2",
    "The Luck-stick Seller",
    "I Want to Forget",
    "A Small Favor",
    "The Star Seal",
    "The Star Seal part 2",
    "The Moon Seal",
    "The Moon Seal part 2",
    "The Sun Seal",
    "The Sun Seal part 2",
    "The Stone With No Name",
    "Watch Your Step",
    "A Simple Question",
    "An Unfamiliar Land",
    "To Whom Gods Bow",
    "Books of Magick",
    "The Ultimate Book",
    "Wanted: Barmaid!",
    "Odd Places",
    "Odd Places part 2",
    "Odd Places part 3",
    "Odd Places part 4",
    "Odd Places part 5",
    "Eternal Rivalry",
    "Crying Eyeball",
    "Hunting Season part 2",
    "Hunting Season part 3",
    "Hunting Season part 4",
    "Hunting Season part 5",
    "Hunting Season part 6",
    "Hunting Season part 7",
    "Hunting Season part 8",
    "Hunting Season part 9",
    "Hunting Season part 10",
    "Hunting Season part 11",
    "Hunting Season part 12",
    "Hunting Season part 13",
    "Hunting Season part 14",
    "Wanted: Tutor!",
    "Strong Lady",
    "Caravan Cry",
    "With a Smile",
    "With a Smile part 2",
    "With a Smile part 3",
    "With a Smile part 4",
    "The Stone With No Name part 2",
    "-",
    "Aid the Serpent",
    "Caravan Cry II",
    "Summons",
    "Three-Point Strategy",
    "Three-Point Strategy part 2",
    "Three-Point Strategy part 3",
    "The Last Duelhorn",
    "Lethean Draught",
    "Devil's Pact",
    "One Last Memory",
    "A Lasting Peace",
    "Kids These Days",
    "Show of Strength",
    "The Way of the Sword",
    "From 'Cross the Sea",
    "From 'Cross the Sea part 2",
    "A Lady's Insistence",
    "Wanted: Hatchery Worker",
    "Death March",
    "Death March, II",
    "Death March, III",
    "Survey No. 258",
    "Survey No. 259",
    "Survey No. 260",
    "Survey No. 261",
    "Champ's Reward",
    "Master's Reward",
    "Champ's Reward part 2",
    "Master's Reward part 2",
    "Champ's Reward part 3",
    "Master's Reward part 3",
    "Champ's Reward part 4",
    "Master's Reward part 4",
    "Champ's Reward part 5",
    "Master's Reward part 5",
    "Wanted: Clan!",
    "Wanted: Clan! part 2",
    "Wanted: Clan! part 3",
    "Wanted: Clan! part 4",
    "Wanted: Clan! part 5",
    "Wanted: Clan! part 6",
    "Wanted: Clan! part 7",
    "Wanted: Clan! part 8",
    "Wanted: Clan! part 9",
    "Wanted: Clan! part 10",
    "Wanted: Clan! part 11",
    "Wanted: Clan! part 12",
    "Wanted: Clan! part 13",
    "Wanted: Clan! part 14",
    "Wanted: Clan! part 15",
    "Wanted: Clan! part 16",
    "Wanted: Clan! part 17",
    "Wanted: Assistant",
    "Wanted: Caretaker",
    "Wanted: Woodworker",
    "Wanted: Woodcutter",
    "Wanted: Combatants",
    "Beneath the Sands",
    "Komodo Search",
    "Jytras Pirata",
    "Jytras Pirata part 2",
    "Jytras Pirata part 3",
    "House Bowen",
    "The Camoa Braves",
    "The Yellow Wings part 2",
    "Graszton Seaways",
    "Galerria Jewelers",
    "Chita's Weaponers",
    "Zedlei Consortium",
    "Zedlei Consortium part 2",
    "Kthili Surveyors",
    "Moogle Porters",
    "Prima Donna",
    "Fey Mischief",
    "One-Eyed Evil",
    "Open Wide",
    "Spirits of Nazan",
    "Formidable Strength",
    "A Bewitching Encounter",
    "Burning Soul",
    "Dire Rotundity",
    "Shaved Ice",
    "Loar Airships Grounded",
    "Ordalia Airships Grounded",
    "Stowaways",
    "The Veluga Pirates",
    "The Camoa Braves part 2",
    "Kthili Surveyors part 2",
    "Arbiters of Death",
    "Jytras Pirata part 4",
    "A Fatal Mistake",
    "House Bowen's Challenge",
    "Ruinous Traps",
    "Wanted: Artillery",
    "Wanted: Marksman",
    "Wanted: Shiny Maces",
    "Picnic Pleasure",
    "A Voice from the Well",
    "Tree Hugging",
    "Our Playground",
    "Teach a Man to Fish",
    "Teach a Man to Run",
    "Komodo Departure",
    "Something's Dropped!",
    "Fluffy Flier?",
    "The Storage Shed",
    "Airship S.O.S.!",
    "Pirate Attack",
    "Kidnapping!?",
    "Mushroom Chef",
    "Komodo Arrival",
    "Thieves in the Ruins",
    "Gimme That!",
    "Oh No, Kupo!",
    "Yellow Wings in Trouble",
    "Rancher's Request 8F Black",
    "Rancher's Request 8F Green",
    "Rancher's Request 8F Brown",
    "Rancher's Request 8F White",
    "The Luck-stick Trader",
    "Seeker of Slaughter",
    "Rancher's Request 8F Red",
    "Wee Evil",
    "The Strength of the Wolf",
    "A Hard Place",
    "Otherworldly Visitors",
    "Just Desserts",
    "Of a Feather",
    "Wanted: Devotees!",
    "Cleaning to Ordalia",
    "Cleaning to Loar",
    "The Final Quest",
    "Detitlement"
]


class QuestData(NamedTuple):
    name: str
    battle: int
    region: int


# (Battle, Region)
questData: List[QuestData] = [
    QuestData("-", 0x0000, 0x00,),
    QuestData("Stranger in the Woods", 0x0001, 0xFF,),
    QuestData("A Paw Full of Feathers", 0x0002, 0xFF,),
    QuestData("The Yellow Wings", 0x0003, 0xFF,),
    QuestData("You Say Tomato", 0x0004, 0xFF,),
    QuestData("Wanted: Ugohr", 0x0005, 0xFF,),
    QuestData("Wanted: Gilmunto", 0x0006, 0xFF,),
    QuestData("Now That's a Fire!", 0x0007, 0xFF,),
    QuestData("Pearls in the Deep", 0x0008, 0xFF,),
    QuestData("Mountain Watch", 0x0009, 0xFF,),
    QuestData("Grounded!", 0x000A, 0xFF,),
    QuestData("Rumors Abound", 0x000B, 0xFF,),
    QuestData("Sleepless Nights", 0x000C, 0xFF,),
    QuestData("Making Music", 0x000E, 0xFF,),
    QuestData("Making Music part 2", 0x000D, 0x00,),
    QuestData("Seeking the Stone", 0x000F, 0xFF,),
    QuestData("Wanted: Sky Pirate Vaan", 0x0010, 0xFF,),
    QuestData("A Request", 0x0011, 0xFF,),
    QuestData("The Rift", 0x0012, 0x80,),
    QuestData("The Dig", 0x0013, 0xFF,),
    QuestData("Through Another's Eyes", 0x0014, 0xFF,),
    QuestData("Pirate Problems", 0x0015, 0xFF,),
    QuestData("The Ritual", 0x0016, 0xFF,),
    QuestData("The Two Grimoires", 0x0017, 0x80,),
    QuestData("From the Rift", 0x0018, 0x80,),
    QuestData("-", 0x0000, 0x80,),
    QuestData("-", 0x0000, 0x80,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("The Search", 0x0000, 0x00,),
    QuestData("Gifted", 0x0019, 0x00,),
    QuestData("An Elegant Encounter", 0x0000, 0x00,),
    QuestData("Where Could He Be?", 0x001A, 0x00,),
    QuestData("A Moment's Respite", 0x0000, 0x00,),
    QuestData("I've Been Had, Kupo!", 0x001B, 0x7F,),
    QuestData("A Refined Recruit", 0x0000, 0x00,),
    QuestData("I'm Back, Kupo!", 0x0000, 0x00,),
    QuestData("Wanted: Friends, Kupo!", 0x0000, 0x7F,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("A Lost Companion", 0x001C, 0x01,),
    QuestData("Help!", 0x0000, 0x01,),
    QuestData("Woman of the Wood", 0x001D, 0x01,),
    QuestData("The Beast of Aisenfield", 0x001E, 0x01,),
    QuestData("Shrine of the Paling Gods", 0x001F, 0x01,),
    QuestData("Bringer of Doom", 0x0020, 0x01,),
    QuestData("Unplumbed Depths", 0x0021, 0x01,),
    QuestData("A Dashing Duel", 0x0022, 0x7F,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("Brightmoon Tor", 0x0174, 0x00,),
    QuestData("Brightmoon Tor, 2nd Ascent", 0x0175, 0x00,),
    QuestData("Brightmoon Tor, 3rd Ascent", 0x0176, 0x00,),
    QuestData("-", 0x0177, 0x00,),
    QuestData("-", 0x0178, 0x00,),
    QuestData("Clan Mates recruit", 0x0000, 0x7F,),
    QuestData("Reagent Run", 0x010B, 0x7F,),
    QuestData("To Be a Fighter", 0x0023, 0x7F,),
    QuestData("The Eastwatch", 0x0024, 0x7F,),
    QuestData("Kyrra, Dragoon", 0x0025, 0x7F,),
    QuestData("Banbanga!", 0x0026, 0x7F,),
    QuestData("The Bangaa Brotherhood", 0x0000, 0x7F,),
    QuestData("Sleight of Hand", 0x0027, 0x7F,),
    QuestData("Knowing the Beast", 0x0028, 0x7F,),
    QuestData("The Nu Mou Nobles", 0x0000, 0x7F,),
    QuestData("Treasured Tomes", 0x0000, 0x7F,),
    QuestData("Veis, Assassin", 0x0029, 0x7F,),
    QuestData("Green Dominion", 0x002A, 0x7F,),
    QuestData("To Be a Spellblade", 0x002B, 0x7F,),
    QuestData("The Goug Consortium", 0x002C, 0x7F,),
    QuestData("Of Kupos and Cannons", 0x002D, 0x7F,),
    QuestData("Popocho's Chocobos", 0x002E, 0x7F,),
    QuestData("Popocho's Chocobos part 2", 0x002F, 0x00,),
    QuestData("Popocho's Chocobos part 3", 0x0030, 0x00,),
    QuestData("A Lanista's Pride", 0x0031, 0x7F,),
    QuestData("Lord Grayrl!", 0x0032, 0x7F,),
    QuestData("Instrument of Inspiration", 0x0033, 0x7F,),
    QuestData("Ravager", 0x0034, 0x7F,),
    QuestData("Geomancer's Way 8F Sun", 0x0035, 0x7F,),
    QuestData("Geomancer's Way 8F Rain", 0x0036, 0x7F,),
    QuestData("Geomancer's Way 8F Snow", 0x0037, 0x7F,),
    QuestData("Geomancer's Way 8F Mist", 0x0038, 0x7F,),
    QuestData("General Training I", 0x008E, 0x7E,),
    QuestData("General Training II", 0x008F, 0x7E,),
    QuestData("Negotiation I", 0x0090, 0x7E,),
    QuestData("Negotiation II", 0x0091, 0x7E,),
    QuestData("Aptitude I", 0x0092, 0x7E,),
    QuestData("Aptitude II", 0x0093, 0x7E,),
    QuestData("Teamwork I", 0x0094, 0x7E,),
    QuestData("Teamwork II", 0x0095, 0x7E,),
    QuestData("Adaptability I", 0x0096, 0x7E,),
    QuestData("Adaptability II", 0x0097, 0x7E,),
    QuestData("Negotiation-Teamwork", 0x0098, 0x7E,),
    QuestData("Adaptability-Negotiation", 0x0099, 0x7E,),
    QuestData("Teamwork-Aptitude", 0x009A, 0x7E,),
    QuestData("Aptitude-Adaptability", 0x009B, 0x7E,),
    QuestData("Bonga Bugle 8E Blackfrost", 0x009C, 0x7F,),
    QuestData("Bonga Bugle 8E Skyfrost", 0x0039, 0x00,),
    QuestData("Bonga Bugle 8E Skyfrost part 2", 0x003A, 0x00,),
    QuestData("Bonga Bugle 8E Skyfrost part 3", 0x003B, 0x00,),
    QuestData("Bonga Bugle 8E Greenfire", 0x003C, 0x00,),
    QuestData("Bonga Bugle 8E Greenfire part 2", 0x003D, 0x00,),
    QuestData("Bonga Bugle 8E Greenfire part 3", 0x003E, 0x00,),
    QuestData("Bonga Bugle 8E Greenfire part 4", 0x003F, 0x00,),
    QuestData("Bonga Bugle 8E Bloodfire", 0x00B1, 0x7F,),
    QuestData("Bonga Bugle 8E Rosefire", 0x0077, 0x7F,),
    QuestData("Bonga Bugle 8E Coppersun", 0x0078, 0x00,),
    QuestData("Bonga Bugle 8E Coppersun part 2", 0x0079, 0x00,),
    QuestData("Bonga Bugle 8E Coppersun part 3", 0x007A, 0x00,),
    QuestData("Bonga Bugle 8E Silversun", 0x007B, 0x3F,),
    QuestData("Bonga Bugle 8E Goldsun", 0x009D, 0x7F,),
    QuestData("Bonga Bugle 8E Ashleaf", 0x007C, 0x7F,),
    QuestData("Bonga Bugle 8E Mistleaf", 0x007D, 0x7F,),
    QuestData("Bonga Bugle 8E Emberleaf", 0x0040, 0x00,),
    QuestData("Bonga Bugle 8E Emberleaf part 2", 0x0041, 0x00,),
    QuestData("Bonga Bugle 8E Emberleaf part 3", 0x0042, 0x00,),
    QuestData("Bonga Bugle 8E Emberleaf part 4", 0x0043, 0x00,),
    QuestData("Bonga Bugle 8E Plumfrost", 0x0044, 0x00,),
    QuestData("Bonga Bugle 8E Plumfrost part 2", 0x0045, 0x00,),
    QuestData("Bonga Bugle 8E Plumfrost part 3", 0x0046, 0x00,),
    QuestData("Wanted: The Cyanwolf", 0x0047, 0x1F,),
    QuestData("Wanted: Lang Bros.", 0x0048, 0x1F,),
    QuestData("Wanted: Big Eyes", 0x0049, 0x1F,),
    QuestData("Wanted: The Mirage Bunny", 0x004A, 0x1F,),
    QuestData("Wanted: Florah", 0x004B, 0x1F,),
    QuestData("Wanted: Tonberrion", 0x004C, 0x61,),
    QuestData("Wanted: Gaitsnipe", 0x004D, 0x1F,),
    QuestData("Wanted: Icicle Ark", 0x004E, 0x61,),
    QuestData("Wanted: Floraxion", 0x004F, 0x1F,),
    QuestData("Wanted: Moogle Rangers", 0x0050, 0x61,),
    QuestData("Wanted: The Mutadragons", 0x0051, 0x1F,),
    QuestData("Wanted: Magick Weapon", 0x0087, 0x1F,),
    QuestData("Camoa Cup", 0x0052, 0x05,),
    QuestData("Camoa Cup part 2", 0x0053, 0x00,),
    QuestData("Camoa Cup part 3", 0x0054, 0x00,),
    QuestData("Graszton Cup", 0x0055, 0x09,),
    QuestData("Graszton Cup part 2", 0x0056, 0x00,),
    QuestData("Graszton Cup part 3", 0x0057, 0x00,),
    QuestData("Moorabella Cup", 0x0058, 0x11,),
    QuestData("Moorabella Cup part 2", 0x0059, 0x00,),
    QuestData("Moorabella Cup part 3", 0x005A, 0x00,),
    QuestData("Fluorgis Cup", 0x005B, 0x21,),
    QuestData("Fluorgis Cup part 2", 0x005C, 0x00,),
    QuestData("Fluorgis Cup part 3", 0x005D, 0x00,),
    QuestData("Goug Cup", 0x005E, 0x41,),
    QuestData("Goug Cup part 2", 0x005F, 0x00,),
    QuestData("Goug Cup part 3", 0x0060, 0x00,),
    QuestData("Loar Cup", 0x0061, 0x1F,),
    QuestData("Loar Cup part 2", 0x0062, 0x00,),
    QuestData("Loar Cup part 3", 0x0067, 0x00,),
    QuestData("Loar Cup part 4", 0x0068, 0x00,),
    QuestData("Loar Cup part 5", 0x0069, 0x00,),
    QuestData("Ordalia Cup", 0x006A, 0x61,),
    QuestData("Ordalia Cup part 2", 0x006B, 0x00,),
    QuestData("Ordalia Cup part 3", 0x006C, 0x00,),
    QuestData("Ordalia Cup part 4", 0x006D, 0x00,),
    QuestData("Ordalia Cup part 5", 0x006E, 0x00,),
    QuestData("Jylland Cup", 0x006F, 0x7F,),
    QuestData("Jylland Cup part 2", 0x0074, 0x00,),
    QuestData("Jylland Cup part 3", 0x0070, 0x00,),
    QuestData("Jylland Cup part 4", 0x0071, 0x00,),
    QuestData("Jylland Cup part 5", 0x0072, 0x00,),
    QuestData("Jylland Cup part 6", 0x0073, 0x00,),
    QuestData("Jylland Cup part 7", 0x0075, 0x00,),
    QuestData("Champions' Cup", 0x0076, 0x7F,),
    QuestData("Beetle in a Haystack", 0x009E, 0x7F,),
    QuestData("Wayward Drake", 0x009F, 0x7F,),
    QuestData("The White of Its Eye", 0x00A0, 0x7F,),
    QuestData("Flown the Coop", 0x00A1, 0x7F,),
    QuestData("It's a Secret to Everybody", 0x00A2, 0x7F,),
    QuestData("Hellhound Astray", 0x00A3, 0x7F,),
    QuestData("My Little Carrot", 0x00A4, 0x7F,),
    QuestData("Bug Hunt", 0x00A5, 0x7F,),
    QuestData("Bug Hunt part 2", 0x00A6, 0x00,),
    QuestData("Bug Hunt part 3", 0x00A7, 0x00,),
    QuestData("A Treasured Heirloom", 0x00A8, 0x7F,),
    QuestData("The Finest Blade", 0x00A9, 0x7F,),
    QuestData("Rancher's Request 8F Yellow", 0x0166, 0x7F,),
    QuestData("Sun-ripened Mayhem", 0x00AA, 0x7F,),
    QuestData("The Witch of the Fens", 0x0000, 0x00,),
    QuestData("Seeding the Harvest", 0x00AB, 0x7F,),
    QuestData("Kupoppy Flower", 0x00AC, 0x7F,),
    QuestData("Maintaining the Balance", 0x00AD, 0x7F,),
    QuestData("The Natural Order", 0x00AE, 0x7F,),
    QuestData("The First Step", 0x0000, 0x7F,),
    QuestData("The Next Step", 0x0000, 0x7F,),
    QuestData("The Next Step part 2", 0x0000, 0x00,),
    QuestData("A Step Further", 0x00AF, 0x7F,),
    QuestData("The Last Step", 0x0000, 0x7F,),
    QuestData("Starstruck", 0x00B0, 0x7F,),
    QuestData("Under the Weather", 0x0000, 0x7F,),
    QuestData("A Chill in the Night", 0x0000, 0x7F,),
    QuestData("Hunted", 0x00B2, 0x7F,),
    QuestData("Past Burdens", 0x00B3, 0x00,),
    QuestData("Rude Awakening", 0x0000, 0x7F,),
    QuestData("Drowsy Draught", 0x0000, 0x7F,),
    QuestData("Inspiration or Perspiration?", 0x00B4, 0x7F,),
    QuestData("For My Love", 0x0000, 0x7F,),
    QuestData("My Secret Shame", 0x00B5, 0x7F,),
    QuestData("The Honorable Thing", 0x00B6, 0x7F,),
    QuestData("Shipping Out", 0x0000, 0x7F,),
    QuestData("Shipping Out part 2", 0x0000, 0x00,),
    QuestData("Prepared with Love", 0x0000, 0x7F,),
    QuestData("Prepared with Love part 2", 0x0000, 0x00,),
    QuestData("Meeting the Quota", 0x00B9, 0x7F,),
    QuestData("The Perfect Gift", 0x0000, 0x7F,),
    QuestData("The Show's Not Over...", 0x0000, 0x7F,),
    QuestData("A Lady's Proposition", 0x00BA, 0x7F,),
    QuestData("Vim, Vigor, and Go", 0x0000, 0x7F,),
    QuestData("The Cat's Meow", 0x00BB, 0x7F,),
    QuestData("Cake: The Recipe", 0x00BC, 0x7F,),
    QuestData("Cake: The Ingredients", 0x0000, 0x7F,),
    QuestData("Cake: The Catastrophe", 0x00BD, 0x7F,),
    QuestData("A Lady's Persistence", 0x00BE, 0x7F,),
    QuestData("Hors D'oeuvre of the Hour", 0x007E, 0x7F,),
    QuestData("Devilish Delight", 0x00BF, 0x7F,),
    QuestData("Shelling Out", 0x00C0, 0x7F,),
    QuestData("Flantastic Finish", 0x00C1, 0x7F,),
    QuestData("The Art of Gastronomy", 0x0088, 0x7F,),
    QuestData("The Trappings of Failure", 0x007F, 0x7F,),
    QuestData("Watching the Watchers", 0x00C2, 0x7F,),
    QuestData("Training Wanted", 0x0089, 0x7F,),
    QuestData("Time to Act", 0x00C3, 0x7F,),
    QuestData("Wish Upon A Star", 0x00C4, 0x7F,),
    QuestData("Plea for Help", 0x00C5, 0x7F,),
    QuestData("Wall of Flame", 0x00C6, 0x7F,),
    QuestData("The Bangaa of the Rupies", 0x00C7, 0x7F,),
    QuestData("The Nu Mou of the Rupies", 0x00C8, 0x7F,),
    QuestData("The Rivalry of the Rupies", 0x00C9, 0x7F,),
    QuestData("A Bride for Montblanc", 0x00CA, 0x7F,),
    QuestData("An Earnest Search", 0x0000, 0x7F,),
    QuestData("An Earnest Quandary", 0x0000, 0x7F,),
    QuestData("An Earnest Quandary part 2", 0x0000, 0x00,),
    QuestData("An Earnest Multitude", 0x0000, 0x7F,),
    QuestData("An Earnest Multitude part 2", 0x0000, 0x00,),
    QuestData("An Earnest Multitude part 3", 0x0000, 0x00,),
    QuestData("An Earnest Delight", 0x00CB, 0x7F,),
    QuestData("An Earnest Delight part 2", 0x0000, 0x00,),
    QuestData("An Earnest Delight part 3", 0x0000, 0x00,),
    QuestData("An Earnest Delight part 4", 0x0000, 0x00,),
    QuestData("Gripped by Fear", 0x0000, 0x7F,),
    QuestData("I Must Have It!", 0x0000, 0x7F,),
    QuestData("It's the Thought", 0x0000, 0x7F,),
    QuestData("'Cross the Sea", 0x0000, 0x7F,),
    QuestData("'Cross the Sea part 2", 0x0000, 0x00,),
    QuestData("Love-struck", 0x0000, 0x7F,),
    QuestData("All Good Things...", 0x0000, 0x7F,),
    QuestData("Stuck in the Muck", 0x00CC, 0x7F,),
    QuestData("One Red Phial", 0x0000, 0x7F,),
    QuestData("'Tis the Season", 0x00CD, 0x7F,),
    QuestData("Unfamiliar Folk", 0x00CE, 0x7F,),
    QuestData("Duelhorn", 0x00CF, 0x7F,),
    QuestData("Making Port", 0x00D0, 0x7F,),
    QuestData("Foodstuffs: Texture", 0x00D1, 0x7F,),
    QuestData("Foodstuffs: Aroma", 0x00D2, 0x7F,),
    QuestData("Foodstuffs: Appearance", 0x00D3, 0x7F,),
    QuestData("Foodstuffs: Nutrition", 0x00D4, 0x7F,),
    QuestData("Foodstuffs: Bon Appetit", 0x00D5, 0x7F,),
    QuestData("The Way of the Meek", 0x00D6, 0x7F,),
    QuestData("What Was Lost", 0x0000, 0x7F,),
    QuestData("The Way of the Timid", 0x00D7, 0x7F,),
    QuestData("Great Land Festival", 0x0157, 0x7F,),
    QuestData("It's a Trap!", 0x00D8, 0x7F,),
    QuestData("Throw Down", 0x008C, 0x7F,),
    QuestData("I Got a Bad Feeling", 0x008B, 0x00,),
    QuestData("Showdown", 0x008A, 0x7F,),
    QuestData("Red King of Cinquleur", 0x00D9, 0x7F,),
    QuestData("Black King of Cinquleur", 0x00DA, 0x7F,),
    QuestData("Green King of Cinquleur", 0x00DB, 0x7F,),
    QuestData("Blue King of Cinquleur", 0x00DC, 0x7F,),
    QuestData("White King of Cinquleur", 0x00DD, 0x7F,),
    QuestData("The Five Kings", 0x00DE, 0x7F,),
    QuestData("Wanted: Sidekick", 0x0159, 0x7F,),
    QuestData("The Wonders of Loar", 0x0000, 0x7F,),
    QuestData("The Wonders of Loar part 2", 0x0000, 0x00,),
    QuestData("The Wonders of Loar part 3", 0x0000, 0x00,),
    QuestData("The Wonders of Loar part 4", 0x0000, 0x00,),
    QuestData("The Camoa Nightwatch", 0x00EA, 0x7F,),
    QuestData("Memories Forged", 0x00E9, 0x7F,),
    QuestData("The Lands of Loar", 0x0000, 0x7F,),
    QuestData("The Lands of Loar part 2", 0x0000, 0x00,),
    QuestData("The Lands of Loar part 3", 0x0000, 0x00,),
    QuestData("The Forests of Loar", 0x0000, 0x7F,),
    QuestData("The Forests of Loar part 2", 0x0000, 0x00,),
    QuestData("The Forests of Loar part 3", 0x0000, 0x00,),
    QuestData("The Towns of Loar", 0x0000, 0x7F,),
    QuestData("The Towns of Loar part 2", 0x0000, 0x00,),
    QuestData("The Towns of Loar part 3", 0x0000, 0x00,),
    QuestData("The Seas of Ordalia", 0x0000, 0x7F,),
    QuestData("The Seas of Ordalia part 2", 0x0000, 0x00,),
    QuestData("The Seas of Ordalia part 3", 0x0000, 0x00,),
    QuestData("The Forgotten Places", 0x0000, 0x7F,),
    QuestData("The Forgotten Places part 2", 0x0000, 0x00,),
    QuestData("The Forgotten Places part 3", 0x0000, 0x00,),
    QuestData("The Forgotten Places part 4", 0x0000, 0x00,),
    QuestData("Bonga Bugle 8E Skyfrost part 4", 0x0000, 0x35,),
    QuestData("Bonga Bugle 8E Greenfire part 5", 0x0000, 0x35,),
    QuestData("Bonga Bugle 8E Coppersun part 4", 0x0000, 0x35,),
    QuestData("Bonga Bugle 8E Emberleaf part 5", 0x0000, 0x35,),
    QuestData("Bonga Bugle 8E Plumfrost part 4", 0x0000, 0x35,),
    QuestData("The Wonders of Ordalia", 0x0000, 0x7F,),
    QuestData("The Wonders of Ordalia part 2", 0x0000, 0x00,),
    QuestData("The Wonders of Ordalia part 3", 0x0000, 0x00,),
    QuestData("For the Cause", 0x0000, 0x7F,),
    QuestData("On the Rampage", 0x00DF, 0x7F,),
    QuestData("Monster Poaching", 0x00E0, 0x7F,),
    QuestData("Poachers Spotted", 0x00E1, 0x7F,),
    QuestData("An Unseen Foe", 0x00E2, 0x7F,),
    QuestData("Memories", 0x0000, 0x7F,),
    QuestData("Abducted!", 0x00E3, 0x7F,),
    QuestData("Graszton Nightwatch", 0x00E4, 0x7F,),
    QuestData("Chita on Weapons8ENovices", 0x00E5, 0x7F,),
    QuestData("Chita on Weapons8EAdepts", 0x00E6, 0x7F,),
    QuestData("Chita on Weapons8EMasters", 0x00E7, 0x7F,),
    QuestData("Cilawa the Gluttonous", 0x0000, 0x7F,),
    QuestData("Escort Wanted", 0x00E8, 0x7F,),
    QuestData("Hunting Season", 0x0000, 0x00,),
    QuestData("Moorabella Nightwatch", 0x00EB, 0x7F,),
    QuestData("Fluorgis Nightwatch", 0x00EF, 0x7F,),
    QuestData("Goug Nightwatch", 0x00F0, 0x7F,),
    QuestData("Shady Dealings", 0x016E, 0x00,),
    QuestData("Drawn Bridge", 0x016D, 0x41,),
    QuestData("A Harvest Hand", 0x0158, 0x7F,),
    QuestData("Speed Battle, Kupo!", 0x0172, 0x7F,),
    QuestData("The Genuine Article", 0x00EC, 0x7F,),
    QuestData("The Root of the Problem", 0x00ED, 0x7F,),
    QuestData("The Whole Truth", 0x00EE, 0x7F,),
    QuestData("Wanted: Musician!", 0x0165, 0x7F,),
    QuestData("A Charm for Luck", 0x0000, 0x7F,),
    QuestData("A Charm for Luck part 2", 0x0000, 0x00,),
    QuestData("The Luck-stick Seller", 0x0000, 0x00,),
    QuestData("I Want to Forget", 0x0171, 0x7F,),
    QuestData("A Small Favor", 0x0000, 0x7F,),
    QuestData("The Star Seal", 0x00F2, 0x7F,),
    QuestData("The Star Seal part 2", 0x00F3, 0x00,),
    QuestData("The Moon Seal", 0x00F4, 0x7F,),
    QuestData("The Moon Seal part 2", 0x00F5, 0x00,),
    QuestData("The Sun Seal", 0x00F6, 0x7F,),
    QuestData("The Sun Seal part 2", 0x00F7, 0x00,),
    QuestData("The Stone With No Name", 0x00F8, 0x7F,),
    QuestData("Watch Your Step", 0x008D, 0x7F,),
    QuestData("A Simple Question", 0x0000, 0x7F,),
    QuestData("An Unfamiliar Land", 0x0000, 0x7F,),
    QuestData("To Whom Gods Bow", 0x0000, 0x7F,),
    QuestData("Books of Magick", 0x0000, 0x7F,),
    QuestData("The Ultimate Book", 0x0000, 0x7F,),
    QuestData("Wanted: Barmaid!", 0x015A, 0x7F,),
    QuestData("Odd Places", 0x00F9, 0x7F,),
    QuestData("Odd Places part 2", 0x00FA, 0x00,),
    QuestData("Odd Places part 3", 0x00FB, 0x00,),
    QuestData("Odd Places part 4", 0x00FC, 0x00,),
    QuestData("Odd Places part 5", 0x00FD, 0x00,),
    QuestData("Eternal Rivalry", 0x00FE, 0x7F,),
    QuestData("Crying Eyeball", 0x0080, 0x7F,),
    QuestData("Hunting Season part 2", 0x0000, 0x7F,),
    QuestData("Hunting Season part 3", 0x0100, 0x00,),
    QuestData("Hunting Season part 4", 0x0101, 0x00,),
    QuestData("Hunting Season part 5", 0x0102, 0x00,),
    QuestData("Hunting Season part 6", 0x0103, 0x00,),
    QuestData("Hunting Season part 7", 0x0104, 0x00,),
    QuestData("Hunting Season part 8", 0x0105, 0x00,),
    QuestData("Hunting Season part 9", 0x0106, 0x00,),
    QuestData("Hunting Season part 10", 0x0107, 0x00,),
    QuestData("Hunting Season part 11", 0x0108, 0x00,),
    QuestData("Hunting Season part 12", 0x0109, 0x00,),
    QuestData("Hunting Season part 13", 0x010A, 0x00,),
    QuestData("Hunting Season part 14", 0x00FF, 0x00,),
    QuestData("Wanted: Tutor!", 0x015B, 0x7F,),
    QuestData("Strong Lady", 0x010C, 0x7F,),
    QuestData("Caravan Cry", 0x010D, 0x7F,),
    QuestData("With a Smile", 0x010E, 0x00,),
    QuestData("With a Smile part 2", 0x010F, 0x00,),
    QuestData("With a Smile part 3", 0x0110, 0x00,),
    QuestData("With a Smile part 4", 0x0111, 0x00,),
    QuestData("The Stone With No Name part 2", 0x016C, 0x00,),
    QuestData("-", 0x0000, 0x00,),
    QuestData("Aid the Serpent", 0x0112, 0x7F,),
    QuestData("Caravan Cry II", 0x0113, 0x7F,),
    QuestData("Summons", 0x0114, 0x7F,),
    QuestData("Three-Point Strategy", 0x0115, 0x7F,),
    QuestData("Three-Point Strategy part 2", 0x0116, 0x00,),
    QuestData("Three-Point Strategy part 3", 0x0117, 0x00,),
    QuestData("The Last Duelhorn", 0x0118, 0x7F,),
    QuestData("Lethean Draught", 0x0119, 0x7F,),
    QuestData("Devil's Pact", 0x011A, 0x7F,),
    QuestData("One Last Memory", 0x011B, 0x7F,),
    QuestData("A Lasting Peace", 0x0000, 0x7F,),
    QuestData("Kids These Days", 0x011C, 0x7F,),
    QuestData("Show of Strength", 0x011D, 0x7F,),
    QuestData("The Way of the Sword", 0x011E, 0x7F,),
    QuestData("From 'Cross the Sea", 0x0000, 0x7F,),
    QuestData("From 'Cross the Sea part 2", 0x0000, 0x00,),
    QuestData("A Lady's Insistence", 0x011F, 0x7F,),
    QuestData("Wanted: Hatchery Worker", 0x015C, 0x7F,),
    QuestData("Death March", 0x0120, 0x7F,),
    QuestData("Death March, II", 0x0121, 0x7F,),
    QuestData("Death March, III", 0x0122, 0x7F,),
    QuestData("Survey No. 258", 0x0123, 0x7F,),
    QuestData("Survey No. 259", 0x0124, 0x7F,),
    QuestData("Survey No. 260", 0x0125, 0x7F,),
    QuestData("Survey No. 261", 0x0126, 0x7F,),
    QuestData("Champ's Reward", 0x0000, 0x00,),
    QuestData("Master's Reward", 0x0000, 0x00,),
    QuestData("Champ's Reward", 0x0000, 0x00,),
    QuestData("Master's Reward", 0x0000, 0x00,),
    QuestData("Champ's Reward", 0x0000, 0x00,),
    QuestData("Master's Reward", 0x0000, 0x00,),
    QuestData("Champ's Reward", 0x0000, 0x00,),
    QuestData("Master's Reward", 0x0000, 0x00,),
    QuestData("Champ's Reward", 0x0000, 0x00,),
    QuestData("Master's Reward", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Clan! recruit", 0x0000, 0x00,),
    QuestData("Wanted: Assistant", 0x015D, 0x7F,),
    QuestData("Wanted: Caretaker", 0x015E, 0x7F,),
    QuestData("Wanted: Woodworker", 0x015F, 0x7F,),
    QuestData("Wanted: Woodcutter", 0x0160, 0x7F,),
    QuestData("Wanted: Combatants", 0x0161, 0x7F,),
    QuestData("Beneath the Sands", 0x0127, 0x7F,),
    QuestData("Komodo Search", 0x0128, 0x7F,),
    QuestData("Jytras Pirata random", 0x0129, 0x00,),
    QuestData("Jytras Pirata random", 0x0081, 0x00,),
    QuestData("Jytras Pirata random", 0x012A, 0x00,),
    QuestData("House Bowen random", 0x012B, 0x00,),
    QuestData("The Camoa Braves random", 0x0082, 0x00,),
    QuestData("The Yellow Wings random", 0x012C, 0x00,),
    QuestData("Graszton Seaways random", 0x012D, 0x00,),
    QuestData("Galerria Jewelers random", 0x012E, 0x00,),
    QuestData("Chita's Weaponers random", 0x012F, 0x00,),
    QuestData("Zedlei Consortium random", 0x0130, 0x00,),
    QuestData("Zedlei Consortium random", 0x0131, 0x00,),
    QuestData("Kthili Surveyors random", 0x0132, 0x00,),
    QuestData("Moogle Porters random", 0x0133, 0x00,),
    QuestData("Prima Donna random", 0x0134, 0x00,),
    QuestData("Fey Mischief", 0x0135, 0x00,),
    QuestData("One-Eyed Evil", 0x0136, 0x00,),
    QuestData("Open Wide", 0x0083, 0x00,),
    QuestData("Spirits of Nazan", 0x0137, 0x00,),
    QuestData("Formidable Strength", 0x0138, 0x00,),
    QuestData("A Bewitching Encounter", 0x0139, 0x00,),
    QuestData("Burning Soul", 0x013A, 0x00,),
    QuestData("Dire Rotundity", 0x013B, 0x00,),
    QuestData("Shaved Ice", 0x0000, 0x7F,),
    QuestData("Loar Airships Grounded", 0x013C, 0x11,),
    QuestData("Ordalia Airships Grounded", 0x013D, 0x21,),
    QuestData("Stowaways", 0x013E, 0x21,),
    QuestData("The Veluga Pirates", 0x013F, 0x00,),
    QuestData("The Camoa Braves", 0x0140, 0x00,),
    QuestData("Kthili Surveyors", 0x0141, 0x00,),
    QuestData("Arbiters of Death", 0x0142, 0x00,),
    QuestData("Jytras Pirata", 0x0143, 0x00,),
    QuestData("A Fatal Mistake", 0x0144, 0x7F,),
    QuestData("House Bowen's Challenge", 0x0145, 0x7F,),
    QuestData("Ruinous Traps", 0x0146, 0x7F,),
    QuestData("Wanted: Artillery", 0x0162, 0x7F,),
    QuestData("Wanted: Marksman", 0x0163, 0x7F,),
    QuestData("Wanted: Shiny Maces", 0x0164, 0x7F,),
    QuestData("Picnic Pleasure", 0x0147, 0x7F,),
    QuestData("A Voice from the Well", 0x0148, 0x7F,),
    QuestData("Tree Hugging", 0x0084, 0x7F,),
    QuestData("Our Playground", 0x0149, 0x7F,),
    QuestData("Teach a Man to Fish", 0x014A, 0x7F,),
    QuestData("Teach a Man to Run", 0x014B, 0x7F,),
    QuestData("Komodo Departure", 0x014C, 0x7F,),
    QuestData("Something's Dropped!", 0x0085, 0x7F,),
    QuestData("Fluffy Flier?", 0x014D, 0x7F,),
    QuestData("The Storage Shed", 0x014E, 0x7F,),
    QuestData("Airship S.O.S.!", 0x014F, 0x7F,),
    QuestData("Pirate Attack", 0x0150, 0x7F,),
    QuestData("Kidnapping!?", 0x0151, 0x7F,),
    QuestData("Mushroom Chef", 0x0086, 0x7F,),
    QuestData("Komodo Arrival", 0x0152, 0x7F,),
    QuestData("Thieves in the Ruins", 0x0153, 0x7F,),
    QuestData("Gimme That!", 0x0154, 0x7F,),
    QuestData("Oh No, Kupo!", 0x0155, 0x7F,),
    QuestData("Yellow Wings in Trouble", 0x0156, 0x7F,),
    QuestData("Rancher's Request 8F Black", 0x0167, 0x7F,),
    QuestData("Rancher's Request 8F Green", 0x0168, 0x7F,),
    QuestData("Rancher's Request 8F Brown", 0x0169, 0x7F,),
    QuestData("Rancher's Request 8F White", 0x016A, 0x7F,),
    QuestData("The Luck-stick Trader", 0x0000, 0x00,),
    QuestData("Seeker of Slaughter", 0x0000, 0x00,),
    QuestData("Rancher's Request 8F Red", 0x016B, 0x7F,),
    QuestData("Wee Evil", 0x0063, 0x00,),
    QuestData("The Strength of the Wolf", 0x0064, 0x00,),
    QuestData("A Hard Place", 0x0065, 0x00,),
    QuestData("Otherworldly Visitors", 0x0066, 0x00,),
    QuestData("Just Desserts", 0x00B7, 0x00,),
    QuestData("Of a Feather", 0x00B8, 0x00,),
    QuestData("Wanted: Devotees!", 0x00F1, 0x7F,),
    QuestData("Cleaning to Ordalia", 0x016F, 0x11,),
    QuestData("Cleaning to Loar", 0x0170, 0x21,),
    QuestData("The Final Quest", 0x0173, 0x00,),
    QuestData("Detitlement", 0x0000, 0x00,),
]
