import { useState } from 'react';
import { Box, Button, Checkbox, FormControl, FormControlLabel, FormGroup, FormLabel, Grid, TextField, Typography, MenuItem } from '@mui/material';
import axios from 'axios';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';
 
const ingredientsList = [
    'Tomato',
    'Milk',
    'Pepper',
    'Chicken Breast',
    'Oatmeal',
    'Eggs',
    'Yogurt with Proteins',
    'Black Chocolate',
    'Sheep Meat',
    'Onion',
    'Pasta',
    'Rice',
    'Couscous',
    'Broccoli',
    'Spinach',
    'Sweet Potato',
    'Quinoa',
    'Salmon',
    'Avocado',
    'Nuts',
    'Cottage Cheese',
    'Cheese'
  ];
 
  const equipmentList = [
    'Bench',
    'Dumbbell',
    'Yoga Mat',
    'Kettlebell',
    'Jump Rope',
    'Resistance Bands',
    'Medicine Ball'
  ];
 
 
const TrainingForm = () => {
  const navigate = useNavigate();
  const [objective, setObjective] = useState('');
  const [ingredients, setIngredients] = useState([]);
  const [materials, setMaterials] = useState([]);
  const [trainingTimes, setTrainingTimes] = useState('');
 
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('////////');
    try {
      // Envoi des données au backend avec Axios
      const response = axios.post(
        'http://127.0.0.1:5000/handle-query',
        {
            question: {
                objective,
                ingredients,
                materials,
                trainingTimes,
            },
            user_id: "2",
        },
        {
            headers: {
                'Content-Type': 'application/json',
            },
        }
    );
      console.log("question");
      console.log('Réponse du serveur:', response.data);
      toast.success('Données envoyées avec succès !');
      navigate('/');
      // Réinitialiser le formulaire après soumission réussie si nécessaire
      setObjective('');
      setIngredients([]);
      setMaterials([]);
      setTrainingTimes('');
    } catch (error) {
      if (error.response) {
          console.error('Erreur du serveur:', error.response.status, error.response.data);
      } else {
          console.error('Erreur lors de la soumission du formulaire:', error);
      }
  }
  };
 
  const handleIngredientChange = (event) => {
    const { value } = event.target;
    setIngredients(
      ingredients.includes(value)
        ? ingredients.filter((item) => item !== value)
        : [...ingredients, value]
    );
  };
 
  const handleEquipmentChange = (event) => {
    const { value } = event.target;
    setMaterials(
      materials.includes(value)
        ? materials.filter((item) => item !== value)
        : [...materials, value]
    );
  };
 
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Choisissez vos préférences d'entraînement
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Objectif d'entraînement</FormLabel>
              <TextField
                fullWidth
                select
                variant="outlined"
                value={objective}
                onChange={(e) => setObjective(e.target.value)}
              >
                <MenuItem value="Lose weight">Lose weight</MenuItem>
                <MenuItem value="Build Muscle">Build Muscle</MenuItem>
                <MenuItem value="Improve Endurance">Improve Endurance</MenuItem>
              </TextField>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Ingrédients disponibles dans votre réfrigérateur</FormLabel>
              <FormGroup>
                {ingredientsList.map((ingredient) => (
                  <FormControlLabel
                    key={ingredient}
                    control={<Checkbox checked={ingredients.includes(ingredient)} onChange={handleIngredientChange} value={ingredient} />}
                    label={ingredient}
                  />
                ))}
              </FormGroup>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Matériaux disponibles</FormLabel>
              <FormGroup>
                {equipmentList.map((equipment) => (
                  <FormControlLabel
                    key={equipment}
                    control={<Checkbox checked={materials.includes(equipment)} onChange={handleEquipmentChange} value={equipment} />}
                    label={equipment}
                  />
                ))}
              </FormGroup>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Nombre de séances d'entraînement par semaine</FormLabel>
              <TextField
                fullWidth
                select
                variant="outlined"
                value={trainingTimes}
                onChange={(e) => setTrainingTimes(e.target.value)}
              >
                <MenuItem value="1">1</MenuItem>
                <MenuItem value="2">2</MenuItem>
                <MenuItem value="3">3</MenuItem>
                <MenuItem value="4">4</MenuItem>
                <MenuItem value="5">5</MenuItem>
                <MenuItem value="6">6</MenuItem>
                <MenuItem value="7">7</MenuItem>
                {/* Ajoutez plus d'options selon vos besoins */}
              </TextField>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary">
              Soumettre
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
};
 
export default TrainingForm;