const express = require('express');
const app = express();
const router = express.Router();
const { exec } = require('child_process');
const cors = require('cors');

// Middleware to parse JSON
app.use(cors());
app.use(express.json());
router.post('/api/predict', async (req, res) => {
    const url = req.body.url;

    if (!url) {
        return res.status(400).json({ error: 'URL is required' });
    }

    // Call Python script
    exec(`python python/predictor.py "${url}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            return res.status(500).json({ error: 'Prediction failed' });
        }

        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return res.status(500).json({ error: 'Python error' });
        }

        const prediction = stdout.trim(); // Should be '0' or '1'
        res.json({ result: prediction });
    });
});
app.use(router);

app.listen(5000, () => {
    console.log('Server running on http://localhost:5000');
});
