import React, { useEffect, useState } from 'react';
import './acceuil.css';
import axios from 'axios';


const Acceuil = () => {
    const [projects, setProjects] = useState([]);
    const [projectslist, setProjectsList] = useState([]);
    const [newp, setNewp] = useState([]);
    const [newaudit, setNewAudit] = useState([]);

    useEffect(() => {
        const fetchprojects = async() =>{
            const { data } = await axios.get("/get-project");
            const directdata = (data.projects[0]);
            setProjects(directdata);
            const projectlists = (data.projects);
            setProjectsList(projectlists);
            // console.log(projectlists._id);
        };
        fetchprojects();
    }, []);

    const HandleCopy = async() =>{
        const newproject = await axios.get("/copy-paste");
        setNewp(newproject)
        // console.log(newproject)
    }

    const HandleBackup = async() =>{
        const newproject = await axios.get("/backup");
        setNewp(newproject)
        // console.log(newproject)
    }

    const HandleAudit = async() =>{
        const audit = await axios.get("/audit");
        setNewAudit(audit)
    }

  return (
    <div className='acceuil'>
        <div className='left'>
            <h2>LISTE DES PROJETS <span>{projectslist.length}</span></h2><br/>
            <div className='projectlist'>
                {projectslist.map(d => (
                    <div>
                        <ul key={d._id}>
                            <li><button>{d.name}</button></li>
                        </ul>

                        <p>LISTE DES JOBS <span>{d.jobsCount}</span></p>
                    </div>
                ))}
            </div>

            {/* <div>
                {projectslist.map(d => (<h2 key={d._id}>JOBS DU PROJET <span>{d.jobsCount}</span></h2>))}
            </div> */}
        </div>

        <div className='right'>
            <div className='topright'>
                <p>Projet <span className='specialcolor1'>{projects.name}</span> créé par <span className='specialcolor1'>{projects.creator}</span> qui a le status <span className='specialcolor1'>"{projects.status}"</span></p>
                <table className='table'>
                    <tr>
                        <th>Description</th>
                        <td>{projects.description}</td>
                    </tr>
                </table>
            </div>
                <h6 className='mb-5'>OPERATIONS SUR LE PROJET</h6>
            <div>
                <button type="button" className="btn btn-secondary me-1" onClick={()=>HandleCopy()}>Copier ou Coller</button>
                <button type="button" className="btn btn-secondary me-1" onClick={()=>HandleBackup()}>Backup</button>
                <button type="button" className="btn btn-secondary" onClick={()=>HandleAudit()}>Audit</button>
            </div>

        </div>
    </div>
  )
}

export default Acceuil