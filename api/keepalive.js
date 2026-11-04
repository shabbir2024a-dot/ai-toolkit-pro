module.exports = async (req, res) => {
  try {
    const start = Date.now();
    const response = await fetch("https://whatsapp-ai-bot-mmb8.onrender.com/health");
    const data = await response.json();
    return res.status(200).json({
      success: true,
      latencyMs: Date.now() - start,
      bot: data,
      timestamp: new Date().toISOString()
    });
  } catch (err) {
    return res.status(500).json({
      success: false,
      error: err.message,
      timestamp: new Date().toISOString()
    });
  }
};
