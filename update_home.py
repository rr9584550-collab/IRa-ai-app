import re

with open('./app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'r') as f:
    content = f.read()

# Replace Quick Actions grid and below with the PDF features
new_content = """        Spacer(modifier = Modifier.height(24.dp))
        
        Text(
            text = "Complete Tools & Features (2026 Edition)",
            color = Color.White,
            fontSize = 18.sp,
            fontWeight = FontWeight.Bold
        )
        Spacer(modifier = Modifier.height(16.dp))
        
        androidx.compose.foundation.lazy.LazyColumn(
            modifier = Modifier.fillMaxWidth().weight(1f),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            item { FeatureCategory("Communication", "WhatsApp, SMS, Email, Emergency SOS", Icons.Default.Chat, Color(0xFF4CAF50)) }
            item { FeatureCategory("Call Tools", "Call, Answer, Reject, Lookup", Icons.Default.Phone, Color(0xFF2196F3)) }
            item { FeatureCategory("Media Tools", "Music, Volume, Media Control", Icons.Default.MusicNote, Color(0xFFE91E63)) }
            item { FeatureCategory("Device Tools", "Alarm, Timer, Flashlight, Battery, Lock", Icons.Default.SettingsCell, Color(0xFFFF9800)) }
            item { FeatureCategory("Files & Photos", "Manage, Zip, Share, Delete, Camera", Icons.Default.Folder, Color(0xFF9C27B0)) }
            item { FeatureCategory("Smart / Generative", "Websites, Images, Research, Coach", Icons.Default.AutoAwesome, Color(0xFF00BCD4)) }
            item { FeatureCategory("Missions", "Autonomous Multi-Step Goals", Icons.Default.RocketLaunch, Color(0xFFF44336)) }
            item { FeatureCategory("Notifications", "Read, Reply, OTP, Missed Calls", Icons.Default.Notifications, Color(0xFFFFC107)) }
            item { FeatureCategory("Maps & My World", "Navigation, Parking, Nearby, Modes", Icons.Default.Map, Color(0xFF8BC34A)) }
            item { FeatureCategory("PC Connect", "Control Laptop/PC from Phone", Icons.Default.Computer, Color(0xFF3F51B5)) }
            item { FeatureCategory("Search & Browser", "Google Search, Web Navigation", Icons.Default.Language, Color(0xFF009688)) }
            item { FeatureCategory("Screen Automation", "Background App Navigation", Icons.Default.SmartToy, Color(0xFF673AB7)) }
            item { FeatureCategory("Connector Tools", "Google, Drive, GitHub, Canva", Icons.Default.Link, Color(0xFF795548)) }
            item { FeatureCategory("Automation & Triggers", "Agar X ho to Y karo (Rules)", Icons.Default.Rule, Color(0xFF607D8B)) }
        }
    }
}

@Composable
fun FeatureCategory(title: String, subtitle: String, icon: ImageVector, iconColor: Color) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .background(Color(0xFF1A1A1A), RoundedCornerShape(16.dp))
            .padding(16.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .size(48.dp)
                .background(iconColor.copy(alpha = 0.2f), CircleShape),
            contentAlignment = Alignment.Center
        ) {
            Icon(icon, contentDescription = title, tint = iconColor)
        }
        Spacer(modifier = Modifier.width(16.dp))
        Column {
            Text(
                text = title,
                color = Color.White,
                fontSize = 16.sp,
                fontWeight = FontWeight.Bold
            )
            Text(
                text = subtitle,
                color = Color.Gray,
                fontSize = 12.sp
            )
        }
    }
}
"""

content = re.sub(r'        Spacer\(modifier = Modifier.height\(24.dp\)\)\n\n        // Quick Actions.*\}', new_content, content, flags=re.DOTALL)

with open('./app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'w') as f:
    f.write(content)
