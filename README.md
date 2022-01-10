
# FOR BJIT ERP Project_Module
## Customize Project Modules

[![N|Solid](https://img.shields.io/badge/Odoo-Made%20with%20%E2%9D%A4%EF%B8%8F%20by%20Shahriar%20Amin-brightgreen)](https://ishahriar94.github.io/)
[![N|Solid](https://img.shields.io/badge/Version-Odoo%2015-informational)](https://github.com/odoo/odoo)




## Tech

- Python
- Odoo ERP Framework v15
- XML
- CSS
- JS

## Installation

# First Thing First 

Find the "project_kanban.js" file from the following directory 

```addons/project/static/src/js/project_kanban.js```

Now Replace the "_openRecord: function()" JS function with my function below 
### here it is 

```javascript
_openRecord: function () {
        const kanbanBoxesElement = this.el.querySelectorAll('.o_project_kanban_boxes a');
        // if (this.selectionMode !== true && kanbanBoxesElement.length) {
        //     kanbanBoxesElement[0].click();
        // } else {
        //     this._super.apply(this, arguments);
        // }
        
        if (this.selectionMode !== true && kanbanBoxesElement.length) {
            this._super.apply(this, arguments);
        }
    }
```

## Modules Installation

First install the module called `my_custom_employee` - 

### Directory -- 

```my_addons/my_custom_employee```

Then install rest of the modules accordingly.
