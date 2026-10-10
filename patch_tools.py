with open('app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'r') as f:
    content = f.read()

imports = """import com.example.data.DatabaseProvider
import com.example.data.LogEntry
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.CoroutineScope"""
content = content.replace('import android.util.Log', 'import android.util.Log\n' + imports)

log_fun = """
    private fun logExecution(toolName: String, detail: String) {
        CoroutineScope(Dispatchers.IO).launch {
            try {
                val db = DatabaseProvider.getDatabase(context)
                db.logDao().insertLog(LogEntry(type = "COMMAND", message = "Executed \$toolName: \$detail"))
            } catch (e: Exception) {
                Log.e("ToolEngine", "Failed to insert log", e)
            }
        }
    }
"""

content = content.replace(
    'class ToolExecutionEngine(private val context: Context) {',
    'class ToolExecutionEngine(private val context: Context) {' + log_fun
)

# Example command logging: play_music
content = content.replace(
    'buildJsonObject { put("status", "success"); put("message", "Media action \$action dispatched successfully") }',
    'logExecution("media_control", action)\n                        buildJsonObject { put("status", "success"); put("message", "Media action \$action dispatched successfully") }'
)

# Volume
content = content.replace(
    'buildJsonObject { put("status", "success"); put("message", "Volume adjusted \$action") }',
    'logExecution("set_volume", action)\n                        buildJsonObject { put("status", "success"); put("message", "Volume adjusted \$action") }'
)

# Call
content = content.replace(
    'buildJsonObject { put("status", "success"); put("message", "Executed answer_call successfully") }',
    'logExecution("answer_call", "Answered call")\n                    buildJsonObject { put("status", "success"); put("message", "Executed answer_call successfully") }'
)

content = content.replace(
    'buildJsonObject { put("status", "success"); put("message", "Executed end_call successfully") }',
    'logExecution("end_call", "Ended call")\n                    buildJsonObject { put("status", "success"); put("message", "Executed end_call successfully") }'
)

with open('app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'w') as f:
    f.write(content)
